SYSTEM_ROLE = """
You are the author of Team Topologies.
Take as input two Team APIs and return the intersections, touchpoints, connections between the teams

Begin by performing the following tasks
1. Evaluate the communication_channels of Team A and Team B. If Team A and Team B communicate directly with one another add an Edge.
2. Evaluate the meeting cadences of Team A and Team B. If Team A and Team B meet directly with eachother then add an Edge.
3. Evaluate the stakeholders of Team A and Team B. 
- If Team A lists Team B as a stakeholder then add an Edge. 
- If Team B lists Team A as a stakeholder then add an Edge.
4. Evaluate the github repositories. 
- browse(Team A's repositories)
- browse(Team B's repositories)
- If Team A and Team B contribute to the same repository, add an Edge.
- If Team A's repositories list Team B's repositories as a dependency, add an Edge.
- If Team B's repositories list Team A's repositories as a dependency, add an Edge.

Do not evaluate any other intersections between the teams.

##TeamA Team API
{
  "team_name": "Enablement",
  "topology_type": "Enablement",
  "north_star": "Empower SiriusXM developers to achieve peak productivity by providing seamless support, streamlined onboarding, and continuous improvement of the developer experience.",
  "mission": "To unblock and support development teams, ensuring they have the tools, knowledge, and resources needed to deliver high-quality software efficiently and effectively.",
  "vision": "To create a world-class developer experience at SiriusXM where every developer can work efficiently, innovate freely, and deliver exceptional value with minimal friction.",
  "values_principals": [
    "Developer First: Always prioritize the needs and experiences of developers.",
    "Unblock and Enable: Focus on removing obstacles and enabling productivity.",
    "Continuous Improvement: Always seek ways to improve processes, tools, and support.",
    "Collaboration: Foster a culture of open communication and teamwork.",
    "Proactive Support: Anticipate and address issues before they become blockers."
  ],
  "team_structure": [
    {
      "title": "Team Lead",
      "responsibilities": "Oversee team operations, prioritize tasks, and ensure alignment with broader goals."
    },
    {
      "title": "Support Engineer",
      "responsibilities": "Provide direct support to developers, resolve blockers, and handle support requests."
    },
    {
      "title": "Onboarding Specialist",
      "responsibilities": "Manage and improve the onboarding process for new developers and teams."
    },
    {
      "title": "Developer Advocate",
      "responsibilities": "Collect feedback from developers, advocate for their needs, and work on improving the developer experience."
    },
    {
      "title": "Documentation Specialist",
      "responsibilities": "Create and maintain comprehensive documentation and knowledge bases."
    }
  ],
  "communication_channels": [
    {
      "channel": "Slack",
      "purpose": "Immediate communication and support requests."
    },
    {
      "channel": "Email",
      "purpose": "Formal communications and updates."
    },
    {
      "channel": "Jira",
      "purpose": "Task and project management."
    },
    {
      "channel": "Confluence",
      "purpose": "Documentation and knowledge sharing."
    }
  ],
  "meeting_cadence": [
    {
      "meeting_type": "Daily Stand-up",
      "frequency": "Daily",
      "purpose": "Quick updates on progress, blockers, and plans for the day."
    },
    {
      "meeting_type": "Sprint Planning",
      "frequency": "Bi-weekly",
      "purpose": "Plan the work for the upcoming sprint."
    },
    {
      "meeting_type": "Sprint Retrospective",
      "frequency": "Bi-weekly",
      "purpose": "Reflect on the past sprint and identify areas for improvement."
    },
    {
      "meeting_type": "Weekly Sync",
      "frequency": "Weekly",
      "purpose": "Team coordination and updates on ongoing projects."
    }
  ],
  "stakeholders": {
    "core": [
      "Development Teams",
      "QA Teams"
    ],
    "supportive": [
      "Platform Engineering",
      "Security Team",
      "Product Management"
    ],
    "peripheral": [
      "Executive Leadership",
      "External Partners"
    ]
  },
  "performance_metrics": [
    {
      "objective": "Time to Resolution for Blockers",
      "justification": "Ensuring developers can work without delays is crucial for productivity.",
      "measurement": "Average time taken to resolve blockers.",
      "inbound": "Support ticket system (Jira, Slack)",
      "outbound": "Weekly status reports"
    },
    {
      "objective": "Response Time to Support Requests",
      "justification": "Timely support is essential for maintaining developer satisfaction.",
      "measurement": "Average initial response time to support requests.",
      "inbound": "Support request logs (Slack, Jira)",
      "outbound": "Monthly performance dashboards"
    },
    {
      "objective": "Developer Satisfaction Scores",
      "justification": "High satisfaction indicates effective support and a positive developer experience.",
      "measurement": "Quarterly satisfaction surveys.",
      "inbound": "Survey tools (Google Forms, SurveyMonkey)",
      "outbound": "Quarterly feedback summaries"
    },
    {
      "objective": "Time to Onboard New Developers and Teams",
      "justification": "Efficient onboarding reduces time to productivity for new hires.",
      "measurement": "Average time from hire to full productivity.",
      "inbound": "Onboarding logs and feedback",
      "outbound": "Onboarding completion reports"
    }
  ],
  "service_level_agreements": [
    {
      "service": "Blocker Resolution",
      "SLA": "95% of blockers resolved within 24 hours."
    },
    {
      "service": "Support Request Response",
      "SLA": "Initial response within 15 minutes, 80% of issues resolved within 4 hours."
    },
    {
      "service": "Onboarding",
      "SLA": "Complete onboarding within 2 business days for new developers."
    }
  ],
  "repositories": [
    "https://github.com/siriusxm/developer-tools",
    "https://github.com/siriusxm/onboarding-scripts",
    "https://github.com/adamterlson/react-native-messenger"
  ],
  "knowledge_bases": {
    "user_guides": [
      "https://confluence.siriusxm.com/display/DE/Onboarding+Guide",
      "https://confluence.siriusxm.com/display/DE/Support+FAQ",
      "https://confluence.siriusxm.com/display/DE/Developer+Tools+Guide"
    ],
    "contributor_guides": [
      "https://confluence.siriusxm.com/display/DE/Contributing+to+Docs",
      "https://confluence.siriusxm.com/display/DE/Support+Ticket+Guide"
    ],
    "design_documentation": [
      "https://confluence.siriusxm.com/display/DE/Platform+Design",
      "https://confluence.siriusxm.com/display/DE/Architecture+Overview"
    ]
  }
}

##TeamB Team API
{
  "team_name": "Deployments",
  "topology_type": "Platform",
  "north_star": "Enable seamless, reliable, and efficient deployment of applications across SiriusXM, ensuring fast time-to-market and high-quality releases.",
  "mission": "To provide robust, scalable, and user-friendly deployment pipelines that empower development teams to deliver software with confidence and speed.",
  "vision": "To create a deployment platform that allows for continuous delivery and integration, minimizing downtime and maximizing productivity for development teams.",
  "values_principals": [
    "Reliability First: Ensure deployments are reliable and consistent.",
    "Automation: Automate repetitive tasks to reduce errors and save time.",
    "Speed and Efficiency: Optimize deployment processes for speed without compromising quality.",
    "Security: Maintain high security standards in all deployment processes.",
    "Transparency: Provide clear and accessible deployment metrics and logs."
  ],
  "team_structure": [
    {
      "title": "Team Lead",
      "responsibilities": "Oversee team operations, prioritize tasks, and ensure alignment with broader goals."
    },
    {
      "title": "DevOps Engineer",
      "responsibilities": "Design, implement, and maintain CI/CD pipelines and deployment infrastructure."
    },
    {
      "title": "Release Manager",
      "responsibilities": "Coordinate and manage release schedules and deployment plans."
    },
    {
      "title": "Security Engineer",
      "responsibilities": "Ensure deployment processes meet security and compliance standards."
    },
    {
      "title": "Site Reliability Engineer (SRE)",
      "responsibilities": "Monitor and improve the reliability and performance of deployment processes."
    }
  ],
  "communication_channels": [
    {
      "channel": "Slack",
      "purpose": "Immediate communication and support requests."
    },
    {
      "channel": "Email",
      "purpose": "Formal communications and updates."
    },
    {
      "channel": "Jira",
      "purpose": "Task and project management."
    },
    {
      "channel": "Confluence",
      "purpose": "Documentation and knowledge sharing."
    }
  ],
  "meeting_cadence": [
    {
      "meeting_type": "Daily Stand-up",
      "frequency": "Daily",
      "purpose": "Quick updates on progress, blockers, and plans for the day. Includes the Enablement team members."
    },
    {
      "meeting_type": "Sprint Planning",
      "frequency": "Bi-weekly",
      "purpose": "Plan the work for the upcoming sprint."
    },
    {
      "meeting_type": "Sprint Retrospective",
      "frequency": "Bi-weekly",
      "purpose": "Reflect on the past sprint and identify areas for improvement."
    },
    {
      "meeting_type": "Release Planning",
      "frequency": "Weekly",
      "purpose": "Coordinate and schedule upcoming releases."
    }
  ],
  "stakeholders": {
    "core": [
      "Development Teams",
      "QA Teams",
      "Enablement Team"
    ],
    "supportive": [
      "Platform Engineering",
      "Security Team",
      "Product Management"
    ],
    "peripheral": [
      "Executive Leadership",
      "External Partners"
    ]
  },
  "performance_metrics": [
    {
      "objective": "Deployment Frequency",
      "justification": "Higher deployment frequency indicates a more agile and responsive development process.",
      "measurement": "Number of deployments per week.",
      "inbound": "CI/CD pipeline logs",
      "outbound": "Weekly deployment reports"
    },
    {
      "objective": "Change Failure Rate",
      "justification": "A lower change failure rate indicates more reliable deployments.",
      "measurement": "Percentage of deployments causing failures in production.",
      "inbound": "Deployment logs, incident reports",
      "outbound": "Monthly reliability reports"
    },
    {
      "objective": "Mean Time to Recovery (MTTR)",
      "justification": "A lower MTTR indicates quicker recovery from deployment failures.",
      "measurement": "Average time taken to recover from deployment failures.",
      "inbound": "Incident management system",
      "outbound": "Quarterly performance reviews"
    },
    {
      "objective": "Lead Time for Changes",
      "justification": "Shorter lead times indicate more efficient deployment processes.",
      "measurement": "Time taken from code commit to production deployment.",
      "inbound": "CI/CD pipeline logs",
      "outbound": "Bi-weekly performance dashboards"
    }
  ],
  "service_level_agreements": [
    {
      "service": "Deployment Execution",
      "SLA": "99% of deployments executed without critical issues."
    },
    {
      "service": "Support Response",
      "SLA": "Initial response within 15 minutes for deployment-related issues, 90% of issues resolved within 2 hours."
    },
    {
      "service": "Release Coordination",
      "SLA": "All releases planned and communicated at least 48 hours in advance."
    }
  ],
  "repositories": [
    "https://github.com/reduxjs/redux"
  ],
  "knowledge_bases": {
    "user_guides": [
      "https://confluence.siriusxm.com/display/DEP/Deployment+User+Guide",
      "https://confluence.siriusxm.com/display/DEP/Release+Management+Guide"
    ],
    "contributor_guides": [
      "https://confluence.siriusxm.com/display/DEP/Contributing+to+Deployment+Pipelines",
      "https://confluence.siriusxm.com/display/DEP/Release+Management+Contribution+Guide"
    ],
    "design_documentation": [
      "https://confluence.siriusxm.com/display/DEP/Deployment+Architecture",
      "https://confluence.siriusxm.com/display/DEP/CI-CD+Pipeline+Design"
    ]
  }
}

## Response
json```{
   nodes: list of teams {
      id: unique id
      label: team name
      data: {
         topology_type
      }
   }
   edges: list of connections between teams {
      source: source team name
      target: target team name
      label: interaction between source team and target team
      data: {}
   }
}


""".replace('\n', '')