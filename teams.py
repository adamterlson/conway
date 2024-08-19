import autogen
import json
import os
from flask import Blueprint, render_template, request, redirect, url_for, jsonify, current_app
from pymongo import MongoClient
from agents.integration_specialist import SYSTEM_ROLE as INTEGRATION_SYSTEM_ROLE
import tempfile

from autogen.coding import LocalCommandLineCodeExecutor

# Create a temporary directory to store the code files.
temp_dir = os.path.join(os.getcwd(), 'temp')
os.makedirs(temp_dir, exist_ok=True)

# Create a local command line code executor.
executor = LocalCommandLineCodeExecutor(
    timeout=10,  # Timeout for each code execution in seconds.
    work_dir=temp_dir,  # Use the temporary directory to store the code files.
)

# Create an agent with code executor configuration.
code_executor_agent = autogen.ConversableAgent(
    "code_executor_agent",
    llm_config=False,  # Turn off LLM for this agent.
    code_execution_config={"executor": executor},  # Use the local command line code executor.
    human_input_mode="ALWAYS",  # Always take human input for this agent for safety.
)

teams_bp = Blueprint('teams', __name__)
llm_config={"model": "gpt-4o-mini"}

# MongoDB connection
# client = MongoClient('localhost', 27017)
# db = client.my_database
# collection = db.my_collection

def load_json_files(directory):
    json_data = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)
                json_data.append(data)
    return json_data

def create_agent_for_team(team):
    print(team)
    return autogen.ConversableAgent(
        name=team['team_name'],
        system_message=f"""
        You are a helpful AI assistant. Solve tasks by using the Team Charter for {team["team_name"]} to offer assistance to others. Provide support by listing the artifacts produced by {team["team_name"]} that feed into the process task or challenge. Include references and specific identification of the artifact provided and not a generic description. Include a reference to the name of the key in the Team Charter. Only present or flow downstream to solve the given challenge. Do not offer anything that your team is not well-equipped to deliver. Do not offer any support that is not backed by a tangible artifact defined in the Team Charter. 
        Examples of artifacts include 1) Code Artifacts—Codebases and Modules, APIs and Libraries 2) Documentation—Technical Documentation, Runbooks 3) Tools and Frameworks—Custom-built tools for CI/CD, monitoring, testing, or deployment that are shared across teams. 4) Best Practices and Standards—Coding Standards, Design Patterns 4) Knowledge and Expertise: Mentoring and Training: One team may provide training sessions or mentorship to another team on specific technologies or practices. Documentation of Lessons Learned: Sharing experiences from past projects, including what worked and what didn’t. 5) Process Artifacts: User Stories and Backlogs: Teams may pass along refined user stories, requirements, or backlogs that another team will implement. Roadmaps and Plans: Strategic plans or roadmaps developed by one team that influence or guide the work of another. 6) Testing Artifacts: Automated Test Suites: Shared test scripts or suites that can be reused by other teams. Performance and Security Assessments: Reports or tools for assessing system performance or security that can benefit multiple teams. 7) Infrastructure and Environments: Shared DevOps Pipelines: Pre-configured CI/CD pipelines or environments that facilitate faster and more consistent deployments. Cloud Infrastructure: Common cloud resources or configurations that multiple teams use. 8) Feedback and Insights: Bug Reports and Issue Tracking: Detailed feedback or bug reports from one team about systems or components they are using, which help improve the overall system. User Feedback: Insights from users that are passed to teams responsible for different parts of a product. 9) Dependencies and Integrations: Versioned Releases: Teams may share specific versions of software or components that other teams rely on. Service Integration Points: Defined endpoints or protocols for integrating different services developed by separate teams.
        Reply "TERMINATE" in the end when everything is done.

Your Team Charter / Team API is:
## Team Charter for {team["team_name"]}
{jsonify(team)}

Respond only in JSON. Do not include anything other than JSON.
No Prose
No header
No "```"
Format of list item:
    source: {team["team_id"]}
    target: target team id
    type: artifact type
    data: artifact name

[]
""",
        description="Representative of team goals and mission. Presents artifacts that can assist other agents in their mission.",
        llm_config=llm_config,
    )

def cached_integration_completion():
    directory = 'sample_data/team_apis'
    teams = load_json_files(directory)
    teamAgents = [create_agent_for_team(team) for team in teams]

    user_proxy = autogen.ConversableAgent(
        name="Admin",
        system_message="Give the task, and send "
        "instructions to writer to refine the blog post.",
        code_execution_config=False,
        llm_config=llm_config,
        human_input_mode="ALWAYS",
    )
    user_proxy_auto = autogen.UserProxyAgent(
        name="User_Proxy_Auto",
        human_input_mode="NEVER",
        is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
        code_execution_config={
            "last_n_messages": 1,
            "work_dir": "tasks",
            "use_docker": False,
        },  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
    )

    writer = autogen.ConversableAgent(
        name="report_agent",
        llm_config=llm_config,
        system_message="You are a report writer. Your job is to combine every tangible artifact each supporting team is delivering into a single report for the customer team. Create a python script that will write a JSON file containing a unified list of all artifacts provided by the other teams.",
        description="Provides a report summarizing the outputs delivered by other agents."
    )
    chats = []
    task = "I am building self-checkout for Best Buy. How will you help me in this mission? My team_id is 6"
    for agent in teamAgents:
        chats.append({
            "sender": user_proxy_auto,
            "recipient": agent,
            "message": task,
            "clear_history": True,
            "silent": False,
            "summary_method": "last_msg",
        })
    # chats.append({
    #     "sender": user_proxy,
    #     "recipient": writer,
    #     "message": """Your job is to combine every tangible artifact each supporting team is delivering into a single report for the customer team. Create a python script that will write a JSON file containing a unified list of all artifacts provided by the other teams. Reply only with the python code. Do not provide additional context or description. Write a new item to the list in the json document for every artifact provided.
        
    #     JSON format: [
    #         source: source team id
    #         target: target team id
    #         type: artifact type
    #         data: artifact name
    #     ] 
        
    #     """,
    #     "clear_history": True,
    #     "silent": False,
    #     "summary_method": "last_msg",
    # })
    chat_results = autogen.initiate_chats(chats)
    json_result = []
    for result in chat_results:
        artifacts = json.loads(result.summary)
        json_result = [*json_result, *artifacts]
    # code = chat_results[len(chat_results)-1].summary
    print('\n\njson_result=======\n\n', json_result)
    # Create a temporary file in the 'temp' directory
    # Create a temporary file in the 'temp' directory
    with tempfile.NamedTemporaryFile(dir=temp_dir, delete=False, mode='w', suffix='.json') as temp_file:
        # Write the JSON array to the temporary file
        json.dump(json_result, temp_file, indent=4)

    # reply = code_executor_agent.generate_reply(messages=[{"role": "user", "content": f"JSON file: {json_result}"}])
    # print('\n\nREPLY============\n\n', reply)
    print(os.listdir(temp_dir))
    # print('File written to', tempfile.name)

    # groupchat = autogen.GroupChat(
    #     agents=[user_proxy, *teamAgents, writer],
    #     messages=[],
    #     max_round=10,
    #     allowed_or_disallowed_speaker_transitions={
    #         user_proxy: [*teamAgents, writer],
    #         engineer: [user_proxy, executor],
    #         writer: [user_proxy],
    #     },
    # )
    # manager = autogen.GroupChatManager(
    #     groupchat=groupchat, llm_config=llm_config
    # )

    # groupchat_result = user_proxy.initiate_chat(
    #     manager,
    #     message=task,
    # )
    # print(groupchat_result)

    # // Create facilitating agent
    # // Get a list of team names
    # // Prompt with iteration through agents
    # // Doc builder HOW TO DO SUMMARY WATCH VIDS
    # // 
    
    # for api in teamAPIs:
    return json_result

@teams_bp.route('/')
def index():
    graph = cached_integration_completion()
    print(graph)
    return render_template('viz2.html', graph=graph)

@teams_bp.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        collection.insert_one({'item': item})
    return redirect(url_for('teams.index'))

