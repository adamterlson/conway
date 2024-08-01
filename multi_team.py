import os
from autogen import AssistantAgent, UserProxyAgent, ConversableAgent, GroupChat, GroupChatManager
llm_config = {"model": "gpt-4o-mini", "api_key": os.environ["OPENAI_API_KEY"]}
assistant = AssistantAgent("assistant", llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy", code_execution_config=False)

with open('Sample_Input_IN.json', 'r') as file:
    teamAAPI = file.read()
with open('Sample_Input_SCO.json', 'r') as file:
    teamBAPI = file.read()

teamAAgent = ConversableAgent(
    "team_a",
    llm_config={"config_list": [llm_config]},
    code_execution_config=False,  # Turn off code execution, by default it is off.
    function_map=None,  # No registered functions, by default it is None.
    human_input_mode="NEVER",  # Never ask for human input.
    system_message=f"""
        You are the single-threaded leader for all aspects of the team.
        Your team's artifacts are documented in the Team API.
        The Team API is in <TeamAPI>
        All responses are in valid JSON.

        <TeamAPI>
            {teamAAPI}
        </TeamAPI>
    """,
    max_consecutive_auto_reply=1
)
teamBAgent = ConversableAgent(
    "team_b",
    llm_config={"config_list": [llm_config]},
    code_execution_config=False,  # Turn off code execution, by default it is off.
    function_map=None,  # No registered functions, by default it is None.
    human_input_mode="NEVER",  # Never ask for human input.
    system_message=f"""
        You are the single-threaded leader for all aspects of the team.
        Your team's artifacts are documented in the Team API.
        The Team API is in <TeamAPI>.
        All responses are in valid JSON.

        <TeamAPI>
            {teamBAPI}
        </TeamAPI>
    """,
    max_consecutive_auto_reply=1
)

communicationsAnalyst = ConversableAgent(
    "comms_analyst",
    llm_config={"config_list": [llm_config]},
    code_execution_config=False,  # Turn off code execution, by default it is off.
    function_map=None,  # No registered functions, by default it is None.
    human_input_mode="NEVER",  # Never ask for human input.
    system_message=f"""
        You are a communications specialist who cares about the InteractionModes between teams that collaborate.
        Your job is to foster efficient communication mechanisms between teams.
        Begin the conversation by asking each team leader for their current communication plan.
        When all communication plans have been provided, summarize the InteractionMode.
        If there is an overlap, include that in the response.
        If there are no shared tools, indicate that in the response.
        Responses should be in JSON format

        <InteractionMode>
            Type: select one of the following
                Collaboration: working closely together with another team
                X-as-a-Service: Consuming or providing something with minimal collaboration
                Facilitating: helping (or being helped by) another team to clear impediments
            Purpose: Outline the shared mission between the teams that will interact.
            TimeDuration: Specify time duration of how long it will take to complete the mission. If mission is eternal, respond with "continuous".
        </InteractionMode>
    """,
    max_consecutive_auto_reply=1
    
)

group_chat = GroupChat(
    agents=[communicationsAnalyst, teamAAgent, teamBAgent],
    messages=[],
    max_round=3,
)
group_chat_manager = GroupChatManager(
    groupchat=group_chat,
    llm_config={"config_list": [{"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}]},
)
chat_result = communicationsAnalyst.initiate_chat(
    group_chat_manager,
    message="""Begin by stating the purpose of your team and how you like to communicate.""",
    summary_method="reflection_with_llm",
    max_turns=6,
)