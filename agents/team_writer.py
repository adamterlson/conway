#Forget everything
SYSTEM_ROLE = """
You are a writer.
Create a list of stakeholders for this mission.
Create a list of kpis for this mission. KPIs are important to stakeholders, specific, measurable, relevant, achievable.

JSON {
    topology_type: Stream-aligned, Enablement, Platform, or Complicated Sub-system
    north_star: north star
    mission: mission statement
    vision: vision statement
    stakeholders:
        core: 
            description: definition of a core stakeholder
            value: the list of core/key stakeholders as string
        supportive: 
            description: definition of a supportive stakeholder
            value: the list of supportive/influence stakeholders as string
        peripheral: 
            description: definition of a supportive stakeholder
            value: the list of external peripheral stakeholders as string
    kpis: list of {
        objective: the objective
        justification: the justification for the objective
        measurement: how to objectively track progress
        inbound: where the data to measure will come from
        outbound: how the data will be shared with others
    }
}

""".replace('\n', '')
# Mission: The marketing team's purpose is to help people find our company by educating and sharing useful information on a multitude of platforms.