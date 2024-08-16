import json
import os
from flask import Blueprint, render_template, request, redirect, url_for, jsonify, current_app
from pymongo import MongoClient
from agents.integration_specialist import SYSTEM_ROLE as INTEGRATION_SYSTEM_ROLE
import autogen

teams_bp = Blueprint('teams', __name__)

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

def cached_integration_completion(teamAPIs):
    # with open('sample_data/Viz3.json') as f:
    #     graph = json.load(f)
    
    # return graph
    llm_config={"model": "gpt-4o-mini"}
    user_proxy = autogen.ConversableAgent(
        name="Admin",
        system_message="Give the task, and send "
        "instructions to writer to refine the blog post.",
        code_execution_config=False,
        llm_config=llm_config,
        human_input_mode="ALWAYS",
    )

    planner = autogen.ConversableAgent(
        name="Planner",
        system_message="Given a task, please determine "
        "what information is needed to complete the task. "
        "Please note that the information will all be retrieved using"
        " Python code. Please only suggest information that can be "
        "retrieved using Python code. "
        "After each step is done by others, check the progress and "
        "instruct the remaining steps. If a step fails, try to "
        "workaround",
        description="Planner. Given a task, determine what "
        "information is needed to complete the task. "
        "After each step is done by others, check the progress and "
        "instruct the remaining steps",
        llm_config=llm_config,
    )

    engineer = autogen.AssistantAgent(
        name="Engineer",
        llm_config=llm_config,
        description="An engineer that writes code based on the plan "
        "provided by the planner.",
    )

    writer = autogen.ConversableAgent(
        name="Writer",
        llm_config=llm_config,
        system_message="Writer."
        "Please write blogs in markdown format (with relevant titles)"
        " and put the content in pseudo ```md``` code block. "
        "You take feedback from the admin and refine your blog.",
        description="Writer."
        "Write blogs based on the code execution results and take "
        "feedback from the admin to refine the blog."
    )

    groupchat = autogen.GroupChat(
        agents=[user_proxy, engineer, writer, planner],
        messages=[],
        max_round=10,
    )
    manager = autogen.GroupChatManager(
        groupchat=groupchat, llm_config=llm_config
    )
    
    task = "Write a blogpost about the stock price performance of "\
    "Nvidia in the past month. Today's date is 2024-04-23."
    groupchat_result = user_proxy.initiate_chat(
        manager,
        message=task,
    )
    print(groupchat_result)

    # // Create facilitating agent
    # // Get a list of team names
    # // Prompt with iteration through agents
    # // Doc builder HOW TO DO SUMMARY WATCH VIDS
    # // 
    
    # for api in teamAPIs:
    return json.loads({ success: True })

@teams_bp.route('/')
def index():
    directory = 'sample_data/team_apis'
    teams = load_json_files(directory)
    graph = cached_integration_completion(teams)
    print(graph)
    return render_template('viz2.html', teams=teams, graph=graph)

@teams_bp.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        collection.insert_one({'item': item})
    return redirect(url_for('teams.index'))
