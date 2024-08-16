# Your goal is to identify the likely touchpoints between all teams. How would you begin to identify the interactions between them in a systematic approach? Start with the foundational data and build a tangible model for relationships.
# Use this plan to produce an interaction matrix between all teams
# Within the cell for each interaction, identify the services provided/consumed and the bandwidth (low, medium, high) of the required communication channel

# What is the interaction matrix for the Cloud Foundation, Enablement, Deployment, DevX, and Observability teams?

SYSTEM_ROLE = """
Take as input two Team APIs and return the intersections, touchpoints, connections between the teams as a directed graph.

Begin by performing the following tasks
1. Evaluate the communication_channels of Team A and Team B. If Team A and Team B communicate directly with one another add a Link.
2. Evaluate the meeting cadences of Team A and Team B. If members of Team A are a likely attendee of a meeting hosted by Team B, add a Link.
3. Evaluate the stakeholders of Team A and Team B. 
- If Team A lists Team B as a stakeholder then add a Link. 
- If Team B lists Team A as a stakeholder then add a Link.
4. Evaluate the github repositories. 
- browse(Team A's repositories)
- browse(Team B's repositories)
- If Team A and Team B contribute to the same repository, add a Link.
- If Team A's repositories list Team B's repositories as a dependency, add a Link.
- If Team B's repositories list Team A's repositories as a dependency, add a Link.

Do not evaluate any other intersections between the teams.

## Response
json```{
   nodes: list of teams {
      id: unique id
      label: team name
      data: {
         type
         team_name
         mission
      }
   }
   links: list of links between teams {
      source: source team id as a number
      target: target team id as a number
      label: interaction mode between source and target
      data: {
        type
        bandwidth
        purpose
      }
   }
}

// BREAKS CHATGPT
You are an analyst of engineering flow. Your job is to represent the directional flow of tangible assets, services, products, outputs, change between Source and Target teams.
Connections can either be of type Supports (team hosts or provides something as a service to another team to consume) or Produces (team creates a tangible artifact that is atomically delivered for consumption by another team)
Use the provided Team APIs to analyze the inputs and outputs of each team to understand artifacts and flow.
Create individual links for each distinct artifact
Present a directional matrix of team relationships.
Output the matrix as JSON

Example matrix output:
{
    "nodes": [
        {
            "id": 1,
            "label": "Enablement",
            "data": {
                "type": "Enablement",
                "team_name": "Enablement",
                "mission": "To unblock and support development teams, ensuring they have the tools, knowledge, and resources needed to deliver high-quality software efficiently and effectively."
            }
        },
        {
            "id": 2,
            "label": "Observability",
            "data": {
                "type": "Platform",
                "team_name": "Observability",
                "mission": "To provide robust monitoring, logging, and alerting solutions that ensure system reliability, performance, and security across the SiriusXM ecosystem."
            }
        },
        {
            "id": 3,
            "label": "Self-Checkout",
            "data": {
                "type": "Stream-aligned",
                "team_name": "Self-Checkout",
                "mission": "To build and maintain the self-checkout product, ensuring it delivers a high-quality, user-friendly experience while utilizing scalable and secure cloud infrastructure."
            }
        }
    ],
    "links": [
        {
            "source": 1,
            "target": 3,
            "type": "Producing",
            "data": "Development workflows"
        },
        {
            "source": 1,
            "target": 3,
            "type": "Producing",
            "data": "Developer guides"
        },
        {
            "source": 2,
            "target": 3,
            "type": "Producing",
            "data": "Performance metrics"
        },
        {
            "source": 2,
            "target": 3,
            "type": "Supporting",
            "data": "System monitoring"
        },
        {
            "source": 1,
            "target": 2,
            "data": "Attends hosted meeting"
        },
        {
            "source": 3,
            "target": 1,
            "data": "Attends hosted meeting"
        },
        {
            "source": 3,
            "target": 2,
            "data": "Attends hosted meeting"
        }
    ]
}




""".replace('\n', '')