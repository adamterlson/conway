# Basic content
TEAM_API_SCHEMA = """
    Team Type: Analyze the team's responsibilities and outputs. Respond with the appropriate Topology for the specified team. Select Stream-aligned, Platform, Enablement, or Complicated Sub-system
        Stream-aligned team: stream-aligned team is defined as a team that is aligned to a flow of work from a segment of the business domain. This type of team is focused on a specific area of the business and is responsible for delivering value to end users through that area.
        Platform:defined as a team that builds and maintains an internal platform designed to accelerate the delivery of other teams by providing self-service APIs, tools, services, and support. The primary goal of a platform team is to reduce cognitive load for stream-aligned teams, enabling them to focus on delivering business value without being burdened by complexities unrelated to their core mission.
        Enablement: a team that works to help other teams overcome obstacles, improve their capabilities, and adopt new practices and technologies. The primary goal of an enablement team is to increase the autonomy and effectiveness of other teams, particularly stream-aligned teams, by providing guidance, expertise, and support.
        Complicated Sub-system: a team that is responsible for developing, maintaining, and evolving a system which requires specialized knowledge and expertise due to its complexity. This complexity may arise from the subsystem's technical nature, domain-specific requirements, or the integration of advanced technologies. 
    
    Mission Charter: A document that outlines the North Star, mission, objectives, scope, stakeholders, and high-level plans for the team. Provides short, descriptive summary of key objectives and the impact on the stakeholder.
    Values Statements: A collection of short, catchy phrases that describe the team's cultural values, ethics, responsibility, character, comradery, love, and joy.
    
    KPIs and Metrics: List of objective measurements that hold the team accountable to achieving its mission and project goals efficiently according to its values. 
    Feedback Mechanisms: Define clear channels and processes for collecting feedback from both internal team members and external stakeholders to foster continuous improvement and ensure alignment with user needs.
        
    Requirements Documentation: Detailed requirements, user stories, or use cases that define what needs to be delivered.
    Design Documents: Detailed designs for specific components or features, including mockups, wireframes, technical specifications, and visual architecture diagrams.
    Deployment Process Documentation: Methodologies, processes, scripts and configuration for deploying the application or system components.
    User Documentation: A web URL for Guides, manuals, or help files for end-users. Content assumes no prior knowledge or access to application or system.
    Technical Documentation: A web URL for In-depth documentation of the system's technical aspects, including APIs, data models, and integration points.

    Project Plan: A timeline or roadmap outlining key milestones, deliverables, and deadlines.
    
    Meeting Cadences: Summaries of routinely scheduled meetings including discussions, decisions, and action items from meetings.
    Communication Plan: A strategy for how the teams will communicate internally and externally, including tools, frequency, channels, and customer support.
    
    Code Repositories: Shared repositories for storing and managing source code.
    Test Plans and Test Cases: Documentation of the testing strategy, including test cases, expected results, and test environments.

    Continuous Improvement Reports: Summaries of retrospective-derived insights including lessons learned, successes, team member shout-outs, upcoming risks, and areas for improvement to people, process, and technology. Includes action item summary with concrete deliverable goals connected with implementing feedback.
    
    Risk Management: Plan detailing potential risks, mitigation strategies, and contingency actions to help the team proactively address challenges that may arise during the project.

    Roles and Responsibilities: List of team members' responsibilities and roles within the project, ensuring clarity on who is accountable for different aspects of the development process.
    Stakeholder Engagement: Details on how stakeholders, such as product owners, end-users, and management, will be engaged throughout the project to gather feedback, ensure alignment, and manage expectations. Includes stakeholder "distance" from the team specified by "nearest", "near", "far", "farthest". Stakeholders at close distance will be engaged more frequently than stakeholders at a greater distance.
"""

ENABLEMENT_TEAM_API = {
    "Team Type": "Enablement",
    "Mission Charter": {
        "North Star": "Enhance the autonomy and effectiveness of other teams.",
        "Mission": "To provide guidance, expertise, and support that helps other teams overcome obstacles and adopt new practices and technologies.",
        "Objectives": [
            "Increase the autonomy of stream-aligned teams.",
            "Facilitate the adoption of best practices and new technologies.",
            "Reduce time and effort needed for teams to overcome challenges."
        ],
        "Scope": "Organization-wide, across all departments and functions.",
        "Stakeholders": ["Stream-aligned teams", "Platform teams", "Management"],
        "High-level plans": "Develop and deliver training, create reusable assets, and provide consulting support."
    },
    "Values Statements": [
        "Empowerment through support",
        "Continuous improvement",
        "Collaboration and teamwork",
        "Innovation and agility",
        "Customer focus"
    ],
    "KPIs and Metrics": [
        {
            "Objective": "Team Autonomy",
            "Metric": "Number of teams achieving self-sufficiency",
            "Target": "80%",
            "Current": "60%"
        },
        {
            "Objective": "Adoption of Best Practices",
            "Metric": "Number of teams adopting recommended practices",
            "Target": "90%",
            "Current": "70%"
        },
        {
            "Objective": "Training Effectiveness",
            "Metric": "Training satisfaction score",
            "Target": "4.5/5",
            "Current": "4.2/5"
        }
    ],
    "Feedback Mechanisms": [
        "Regular surveys of supported teams",
        "Feedback sessions during retrospectives",
        "Direct input from team leads"
    ],
    "Requirements Documentation": [
        "User stories for enablement initiatives",
        "Use cases for support requests"
    ],
    "Design Documents": [
        "Blueprints for training programs",
        "Technical specifications for reusable assets"
    ],
    "Deployment Process Documentation": [
        "Guidelines for deploying enablement tools",
        "Scripts for automating deployment processes"
    ],
    "User Documentation": "https://example.com/user-guides",
    "Technical Documentation": "https://example.com/technical-docs",
    "Project Plan": [
        {
            "Milestone": "Initial Assessment",
            "Deliverable": "Assessment report",
            "Deadline": "Q1 2024"
        },
        {
            "Milestone": "Pilot Programs",
            "Deliverable": "Pilot enablement programs",
            "Deadline": "Q2 2024"
        },
        {
            "Milestone": "Full Rollout",
            "Deliverable": "Organization-wide enablement support",
            "Deadline": "Q4 2024"
        }
    ],
    "Meeting Cadences": [
        {
            "Meeting Type": "Weekly check-ins",
            "Discussion Points": "Progress updates, feedback collection",
            "Action Items": "Address emerging issues, plan next steps"
        },
        {
            "Meeting Type": "Monthly retrospectives",
            "Discussion Points": "Review successes and challenges, gather insights",
            "Action Items": "Implement improvements"
        }
    ],
    "Communication Plan": [
        "Internal: Weekly updates via email, dedicated Slack channel",
        "External: Monthly newsletters, webinars, customer support portal"
    ],
    "Code Repositories": [
        "GitHub: https://github.com/enablement-team"
    ],
    "Test Plans and Test Cases": [
        "Unit tests for enablement tools",
        "Integration tests for support processes"
    ],
    "Continuous Improvement Reports": [
        {
            "Lessons Learned": "Document common challenges and solutions",
            "Successes": "Highlight successful enablement initiatives",
            "Upcoming Risks": "Identify potential future obstacles",
            "Areas for Improvement": "Suggest enhancements to enablement strategies"
        }
    ],
    "Risk Management": [
        "Potential Risk": "High demand for enablement support",
        "Mitigation Strategy": "Prioritize high-impact areas, expand enablement team"
    ],
    "Roles and Responsibilities": [
        {
            "Role": "Enablement Lead",
            "Responsibilities": "Oversee enablement strategy, coordinate with other teams"
        },
        {
            "Role": "Enablement Specialist",
            "Responsibilities": "Provide expertise, develop training materials, support teams"
        },
        {
            "Role": "Technical Writer",
            "Responsibilities": "Create and maintain user and technical documentation"
        }
    ],
    "Stakeholder Engagement": {
        "Nearest": ["Stream-aligned team leads"],
        "Near": ["Platform team leads"],
        "Far": ["Management"],
        "Farthest": ["External partners"]
    }
}


MISSION_STATEMENT_1 = "The marketing team's purpose is to help people find our company by educating and sharing useful information on a multitude of platforms."
MISSION_STATEMENT_2 = "Our mission is to empower every person and every organization on the planet to achieve more."


OUTPUT_GRAPH = """
Generate additional sample data representing the definition of Team APIs and connections with Interaction Modes in a graph format.

Example:
{
    "nodes": [
        {
            "id": 1,
            "type": "Stream-aligned",
            "mission": "To build the new InterNations mobile application"
        },
        {
            "id": 2,
            "type": "Platform",
            "mission": "To build reusable components that application development teams can use to accelerate delivery and adherence to standards"
        },
        {
            "id": 3,
            "type": "Enablement",
            "mission": "To provide engineering knowledge, best-practices, and guidelines for application development teams"
        }
    ],
    "links": [
        {
            "source": 2,
            "target": 1,
            "value": {
                "type": "X-as-a-Service",
                "bandwidth": "Low",
                "duration": "Continuous",
                "purpose": "Build reusable components that accelerate delivery of InterNations mobile application"
            }
        },
        {
            "source": 3,
            "target": 1,
            "value": {
                "type": "Facilitating",
                "bandwidth": "High",
                "duration": "Two Months",
                "purpose": "Support the onboarding of new team members learning unfamiliar mobile development technologies"
            }
        }
    ]
}
"""