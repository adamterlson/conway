import os
from autogen import AssistantAgent, UserProxyAgent, ConversableAgent, GroupChat, GroupChatManager
llm_config = {"model": "gpt-4o-mini", "api_key": os.environ["OPENAI_API_KEY"]}
assistant = AssistantAgent("assistant", llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy", code_execution_config=False)

conway = ConversableAgent(
    "team_api_writer",
    llm_config={"config_list": [llm_config]},
    code_execution_config=False,  # Turn off code execution, by default it is off.
    function_map=None,  # No registered functions, by default it is None.
    human_input_mode="NEVER",  # Never ask for human input.
    system_message=f"""
        You are a Team API writer and designer. 
        Your goal is to assist the user in the construction and completion of a Team API specification. 
        The description for a Team API is defined in <TeamAPI>.
        Responses contain complete and well-structured Team API definition.
        Responses end with a suggestion for how to better complete each section of the Team API.
        Responses are valid JSON.
        Do not respond until the Team API is nearly complete.
        
        <TeamAPI>
            Topology: Identify Stream-aligned, Platform, Enablement, or Complicated Sub-system
        
            Mission Charter: A document that outlines the North Star, mission, objectives, scope, stakeholders, and high-level plans for the team. Provides short, descriptive summary of key objectives and the impact on the stakeholder.
                Purpose: To provide a clear and shared understanding of team mission and goals.
            
            Values Statements: A collection of single sentences or short phrases that make the reader feel engaged and connected which describe the team's culture, including values, ethics, responsibility, character, love, and joy.
            
            KPIs and Metrics: Real-time report containing the objective measurements that hold the team accountable to achieving its mission and project goals efficiently according to its values. 
                Health Check: If goals are being met on time and within budget, respond Green. If goals are at risk but achievable, respond Yellow. If goals are not being met or at great risk in the near future, respond Red.
                Qualitative Feedback
                    Insight
                Quantitative Feedback
                    Target
                    Current
                
            Requirements Documentation: Detailed requirements, user stories, or use cases that define what needs to be achieved.
            
            Design Documents: Detailed designs for specific components or features, including mockups, wireframes, technical specifications, and visual architecture diagrams.
            
            Project Plan: A timeline or roadmap outlining key milestones, deliverables, and deadlines.
            
            Meeting Cadences: Summaries of routinely scheduled meetings including discussions, decisions, and action items from meetings.
                
            Communication Plan: A strategy for how the teams will communicate internally and externally, including tools, frequency, channels, and customer support.
            
            Code Repositories: Shared repositories for storing and managing source code.
            
            Test Plans and Test Cases: Documentation of the testing strategy, including test cases, expected results, and test environments.
            
            Deployment Processes: Methodologies, processes, scripts and configuration for deploying the application or system components.
            
            User Documentation: A web URL for Guides, manuals, or help files for end-users. Content assumes no prior knowledge or access to application or system.
            
            Technical Documentation: A web URL for In-depth documentation of the system's technical aspects, including APIs, data models, and integration points.
        
            Continuous Improvement Reports: Summaries of retrospective-derived insights including lessons learned, successes, team member shout-outs, upcoming risks, and areas for improvement to people, process, and technology. Includes action item summary with concrete deliverable goals connected with implementing feedback.
                Action Items: A summary of opportunities for change based on provided Feedback
                Feedback:
                    DateCreated: The date this feedback was collected
                    Stop: Summary of behaviors or actions the team identifies as necessary to stop doing. Stop behaviors should be sufficiently described, actionable, measurable, and specific.
                    Start: Opportunities for change that the team identifies as necessary to start doing. Start behaviors should be sufficiently described, actionable, measurable, and specific.
                    Continue: Behaviors the team identifies as necessary to continue doing.
            
            Roles and Responsibilities: List of team members' responsibilities and roles within the project, ensuring clarity on who is accountable for different aspects of the development process.

            Risk Management: Plan detailing potential risks, mitigation strategies, and contingency actions to help the team proactively address challenges that may arise during the project.

            Feedback Mechanisms: Define clear channels and processes for collecting feedback from both internal team members and external stakeholders to foster continuous improvement and ensure alignment with user needs.

            Stakeholder Engagement: Details on how stakeholders, such as product owners, end-users, and management, will be engaged throughout the project to gather feedback, ensure alignment, and manage expectations. Includes stakeholder "distance" from the team specified by "nearest", "near", "far", "farthest". Stakeholders at close distance will be engaged more frequently than stakeholders at a greater distance.
        </TeamAPI>
    """
)
conway.description = "Take human input and continuously refine and complete a Team API"
apiCritic = ConversableAgent(
    "team_api_critic",
    llm_config={"config_list": [llm_config]},
    code_execution_config=False,  # Turn off code execution, by default it is off.
    function_map=None,  # No registered functions, by default it is None.
    human_input_mode="NEVER",  # Never ask for human input.
    system_message=f"""
        You are a critic of Team APIs.
        If the Team API is of good quality, do not respond.
        When the user providers a Team API specification, respond with a summary of areas of improvement in quality, specificity, and completeness.
        If a Team API is not provided, respond with "No Team API provided."
    """
)
apiCritic.description = "Respond to a provided Team API with feedback on how to improve."
human_proxy = ConversableAgent(
    "human_proxy",
    llm_config=False,  # no LLM used for human proxy
    human_input_mode="ALWAYS",  # always ask for human input
)
human_proxy.description = "Respond to the team_api_critic with updated information about the Team API"
changeAnalyst = ConversableAgent(
    "change_analyst",
    llm_config={"config_list": [llm_config]},
    code_execution_config=False,  # Turn off code execution, by default it is off.
    function_map=None,  # No registered functions, by default it is None.
    human_input_mode="NEVER",  # Never ask for human input.
    system_message=f"""
        You are an analyst of organizational and technological Change. Your job is to respond with a complete summary of Change impacts on the team to give specific targeted understanding of advantages, challenges, and risks.
        The Current Team API is in <ImpactedTeamAPI>
        If the user provides a proposed Change, identify the properties of the TeamAPI that will need to change to pivot to accomplish the new objective or outcome.
        Begin by creating a NewTeamAPI which implements Change
        Compare the NewTeamAPI against the ImpactedTeamAPI
        Do not give a response unless you have created your own Team API implementing the Change.
        Response must be in valid JSON format.
    
        <ImpactedTeamAPI>
        </ImpactedTeamAPI>
        
        <Response Format>
            New Team API: The NewTeamAPI
            Change Complexity Score: specify low, medium, or high complexity to implement the Change. Base the score on the number and type of differences between the ImpactedTeamAPI and the NewTeamAPI
            Challenges: compared to the current state, identify the reasons the Change is complex, expensive, or untenable. Includes specific risks identified by the Change that uniquely impact this team and how. Be as specific and complete as possible.
            Advantages: compared to the current state, identify the reasons why the Change is beneficial and positive, including how they align with the ImpactedTeamAPI's mission, values, and project goals. Be as specific and complete as possible.
            Change Impact Areas: compare the ImpactedTeamAPI to the NewTeamAPI. respond with the specific JSON keys that are affected by the Change and a summary of the change.
        </Response Format>
    """
)

# Start the chat
# chat_result = apiCritic.initiate_chat(
#     conway,
#     message="""
#         My team's goal is to build a new InterNations mobile app. Our team members are cross-functional including product, engineering and desisgn. Our values include 'Artifacts are king', 'Make it work, make it right, make it fast.' and 'Security first, defence in depth.' 
#         My team has two squads, one for frontend development and one for the backend. We also have a dedicated QA team.
#      """,
#     summary_method="reflection_with_llm",
#     max_turns=2,
# )

group_chat = GroupChat(
    agents=[human_proxy, conway, apiCritic],
    messages=[],
    max_round=6,
)
group_chat_manager = GroupChatManager(
    groupchat=group_chat,
    llm_config={"config_list": [llm_config]},
)
chat_result = apiCritic.initiate_chat(
    group_chat_manager,
    message="""
        My team's goal is to build a new InterNations mobile app. Our team members are cross-functional including product, engineering and desisgn. Our values include 'Artifacts are king', 'Make it work, make it right, make it fast.' and 'Security first, defence in depth.' 
        My team has two squads, one for frontend development and one for the backend. We also have a dedicated QA team.
     """,
    summary_method="reflection_with_llm",
    max_turns=6,
)