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
            Team Type: Analyze the team's responsibilities and outputs. Respond with the appropriate Topology for the specified team. Select Stream-aligned, Platform, Enablement, or Complicated Sub-system
                Stream-aligned team: stream-aligned team is defined as a team that is aligned to a flow of work from a segment of the business domain. This type of team is focused on a specific area of the business and is responsible for delivering value to end users through that area.
                Platform:defined as a team that builds and maintains an internal platform designed to accelerate the delivery of other teams by providing self-service APIs, tools, services, and support. The primary goal of a platform team is to reduce cognitive load for stream-aligned teams, enabling them to focus on delivering business value without being burdened by complexities unrelated to their core mission.
                Enablement: a team that works to help other teams overcome obstacles, improve their capabilities, and adopt new practices and technologies. The primary goal of an enablement team is to increase the autonomy and effectiveness of other teams, particularly stream-aligned teams, by providing guidance, expertise, and support.
                Complicated Sub-system: a team that is responsible for developing, maintaining, and evolving a system which requires specialized knowledge and expertise due to its complexity. This complexity may arise from the subsystem's technical nature, domain-specific requirements, or the integration of advanced technologies. 
            
            Mission Charter: A document that outlines the North Star, mission, objectives, scope, stakeholders, and high-level plans for the team. Provides short, descriptive summary of key objectives and the impact on the stakeholder.
            
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
        </TeamDefinition>
     """},
    {"role": "user", "content": """
        My team's goal is to build mobile self-checkout. Our team members are cross-functional including product, engineering and desisgn. Our values include 'Artifacts are king', 'Make it work, make it right, make it fast.' and 'Security first, defence in depth.' 
        My team receives support from the Azure Platform team, including with cloud infrastructure management and responding to critical incidents.
        My customer is the Best Buy customer typically under the age of 25 and male. They are tech-savvy and care about digital native experiences. They are motivated by convenience and low friction in accomplishing their goals.
     """}
    # {"role": "user", "content": """
    #     My team's goal is to support the AWS cloud platform. We are building the product as a platform in service to application development teams across the organization.
    #     Our primary responsibility to is to accelerate and support the adoption of cloud native and devops practices.
    #     We evolve shared cloud platform capabilities such as identity services, observability tooling, financial reporting, and cloud foundation capabilities.
    #     Reusable infrastructure as code patterns are published to the following github repository: https://github.com/awslabs/aws-service-catalog-products
    #     Our team is made up of cloud platform engineers, operations engineers, system administrators, and documentation writers.
    #     Our primary product is the developer portal, which provides self-service capabilities for application developers to perform common engineering tasks with minimal friction and cognitive load.
    #  """}
  ]
)

content = json.dumps(json.loads(completion.choices[0].message.content), indent=2)
base_string = "Sample_Output"
current_date = datetime.now()
formatted_datetime = current_date.strftime("%Y%m%d_%H%M%S")
filename = f"{base_string}_{formatted_datetime}.json"
print(content)
with open(filename, 'w') as f:
    print(content, file=f)