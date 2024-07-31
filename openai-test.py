import json

from openai import OpenAI
client = OpenAI()


# You are a team structure specialist. You document and define the responsibilities of teams. You speak with a communications specialist to understand how to communicate with other teams. When sent a resource, assess the content and respond with either  "Platform Team" or "Stream-aligned Team". Do not respond with content other than 

#         If the resource reflects a primary stream of business value that does not provide a service to other parts of the same organization and delivers value directly to the customer, respond with "Stream-aligned Team". The resource should reflect the definition of "Stream-aligned Team" from the book team topologies.

#         If the resource is providing a service to other engineering teams and does not directly touch the customer, respond with "Platform Team". The resource should reflect the definition of "Platform Team" from the book team topologies.

#         If you are not confident, respond "Unknown" with a reason the answer could not be determined.


    #  model Team {
    #     name: string,
    #     mission_statement: string,
    #     goals_kpis: string,
    #     performance_monitors: string,
    #     code_repositories: string[],
    #     communication_channels: InteractionMode[],
    #     routines: [Task],
    #     service_catalog: Service[]]
    #     knowledge_bases: Doc[]
    #     member_roles: MemberRole[]
    #     project_management: string,
    #     financial_report: string,
    #  }

    #  model InteractionMode {
    #     channel_name: string,
    #     channel_bandwidth: 'low' | 'medium' | 'high'
    #     channel_type: 'chat' | 'request'
    #     log: string,
    #  }

    #  model Task {
     
    #  }

    #  model Service {
     
    #  }

    #  model Docs {
    #     tests: string,
    #     contribution: string,
    #     release: string,
    #     operating_model: string,
    #  }

    #  model MemberRole {
     
    #  }

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": """
    You are a Team API architect and designer. Your goal is to assist the user in the construction and completion of a Team API specification. The description for a Team API is defined in <TeamDefinition>.
    
    Responses contain complete and well-structured Team API definition
    Responses end with a suggestion for how to better complete each section of the Team API.
    Responses are valid JSON
    
    
    <TeamDefinition>
     
        Mission Charter:

            Description: A document that outlines the North Star, mission, objectives, scope, stakeholders, and high-level plans for the team. Provides short, descriptive summary of key objectives and the impact on the stakeholder.
            Purpose: To provide a clear and shared understanding of team mission and goals.
        
        Values Statements:
        
            Description: A collection of single sentences or short phrases that make the reader feel engaged and connected which describe the team's culture, including values, ethics, responsibility, character, love, and joy.
        
        KPIs and Metrics:
        
            Description: Real-time report containing the objective measurements that hold the team accountable to achieving its mission and project goals efficiently according to its values. 
            
        Requirements Documentation:

            Description: Detailed requirements, user stories, or use cases that define what needs to be achieved.
        
        Design Documents:

            Description: Detailed designs for specific components or features, including mockups, wireframes, technical specifications, and visual architecture diagrams.
        
        Project Plan:

            Description: A timeline or roadmap outlining key milestones, deliverables, and deadlines.
        
        Meeting Cadences:

            Description: Summaries of routinely scheduled meetings including discussions, decisions, and action items from meetings.
            
        Communication Plan:

            Description: A strategy for how the teams will communicate internally and externally, including tools, frequency, channels, and customer support.
            
        Progress Reports:

            Description: Regular updates on the status of the team toward KPIs and Metrics, including completed tasks, upcoming work, and any issues or risks.
        
        Code Repositories:

            Description: Shared repositories for storing and managing source code.
        
        Test Plans and Test Cases:

            Description: Documentation of the testing strategy, including test cases, expected results, and test environments.
        
        Deployment Processes:

            Description: Methodologies, processes, scripts and configuration for deploying the application or system components.
        
        User Documentation:

            Description: Guides, manuals, or help files for end-users. Content assumes no prior knowledge or access to application or system.
            Structure: A web URL
        
        Technical Documentation:

            Description: In-depth documentation of the system's technical aspects, including APIs, data models, and integration points.
            Structure: A web URL
     
        Continuous Improvement Reports:
     
            Description: Summaries of retrospective-derived insights including lessons learned, successes, team member shout-outs, upcoming risks, and areas for improvement to people, process, and technology. Includes action item summary with concrete deliverable goals connected with implementing feedback.
            Structure:
                Action Items: A summary of opportunities for change based on provided Feedback
                Feedback:
                    DateCreated: The date this feedback was collected
                    Stop: Summary of behaviors or actions the team identifies as necessary to stop doing. Stop behaviors should be sufficiently described, actionable, measurable, and specific.
                    Start: Opportunities for change that the team identifies as necessary to start doing. Start behaviors should be sufficiently described, actionable, measurable, and specific.
                    Continue: Behaviors the team identifies as necessary to continue doing.
        
    </TeamDefinition>
     """},
    {"role": "user", "content": "My team's goal is to build mobile self-checkout and provide new ways for customers to purchase products from our store. Our github is https://github.com/microsoft."}
  ]
)

print(json.dumps(json.loads(completion.choices[0].message.content), indent=2))