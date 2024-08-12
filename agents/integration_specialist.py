# Your goal is to identify the likely touchpoints between all teams. How would you begin to identify the interactions between them in a systematic approach? Start with the foundational data and build a tangible model for relationships.
# Use this plan to produce an interaction matrix between all teams
# Within the cell for each interaction, identify the services provided/consumed and the bandwidth (low, medium, high) of the required communication channel

# What is the interaction matrix for the Cloud Foundation, Enablement, Deployment, DevX, and Observability teams?

SYSTEM_ROLE = """
Take as input two Team APIs and return the intersections, touchpoints, connections between the teams as a directed graph.

Begin by performing the following tasks
1. Evaluate the communication_channels of Team A and Team B. If Team A and Team B communicate directly with one another add a Link.
2. Evaluate the meeting cadences of Team A and Team B. If Team A and Team B meet directly with eachother then add a Link.
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


""".replace('\n', '')