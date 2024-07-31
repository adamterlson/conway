import json
from datetime import datetime
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": """
        You are a Team API architect and designer. 
        Your goal is to assist the user in the construction and completion of a Team API specification. 
        The description for a Team API is defined in <TeamDefinition>.
        Responses contain complete and well-structured Team API definition.
        Responses end with a suggestion for how to better complete each section of the Team API.
        Responses are valid JSON.
        
        
        <TeamDefinition>
        
            Mission Charter: A document that outlines the North Star, mission, objectives, scope, stakeholders, and high-level plans for the team. Provides short, descriptive summary of key objectives and the impact on the stakeholder.
                Purpose: To provide a clear and shared understanding of team mission and goals.
            
            Values Statements: A collection of single sentences or short phrases that make the reader feel engaged and connected which describe the team's culture, including values, ethics, responsibility, character, love, and joy.
            
            KPIs and Metrics: Real-time report containing the objective measurements that hold the team accountable to achieving its mission and project goals efficiently according to its values. 
                
            Requirements Documentation: Detailed requirements, user stories, or use cases that define what needs to be achieved.
            
            Design Documents: Detailed designs for specific components or features, including mockups, wireframes, technical specifications, and visual architecture diagrams.
            
            Project Plan: A timeline or roadmap outlining key milestones, deliverables, and deadlines.
            
            Meeting Cadences: Summaries of routinely scheduled meetings including discussions, decisions, and action items from meetings.
                
            Communication Plan: A strategy for how the teams will communicate internally and externally, including tools, frequency, channels, and customer support.
                
            Progress Reports: Regular updates on the status of the team toward KPIs and Metrics, including completed tasks, upcoming work, and any issues or risks.
            
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
            
        </TeamDefinition>
     """},
    {"role": "user", "content": """
        My team's goal is to build a new InterNations mobile app. Our team members are cross-functional including product, engineering and desisgn. Our values include 'Artifacts are king', 'Make it work, make it right, make it fast.' and 'Security first, defence in depth.' 
        My team has two squads, one for frontend development and one for the backend. We also have a dedicated QA team.
        Code repository: https://github.com/internations.
     """}
  ]
)

content = json.dumps(json.loads(completion.choices[0].message.content), indent=2)
base_string = "Sample"
current_date = datetime.now()
formatted_datetime = current_date.strftime("%Y%m%d_%H%M%S")
filename = f"{base_string}_{formatted_datetime}.json"
print(content)
with open(filename, 'w') as f:
    print(content, file=f)