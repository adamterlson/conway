from typing import List, Optional
from pydantic import BaseModel

class TeamStructure(BaseModel):
    title: str
    responsibilities: str

class CommunicationChannel(BaseModel):
    channel: str
    purpose: str

class Routines(BaseModel):
    frequency: str
    purpose: str
    participants: str

class PerformanceMetric(BaseModel):
    objective: str
    measurement: str
    data_source: str

class ServiceLevelAgreement(BaseModel):
    service: str
    sla: str

class KnowledgeBase(BaseModel):
    user_guides: List[str]
    contribution_guides: List[str]
    design_guides: List[str]
    testing_guides: List[str]

class Stakeholders(BaseModel):
    core: List[str]
    supportive: List[str]
    peripheral: List[str]

class TeamAPI(BaseModel):
    # A unique identifier for the team
    team_id: int
    # The name of the team
    team_name: str
    # According to Matthew Skelton of Team Topologies, is this a Stream-aligned, Enablement, Platform, or Complicated Sub-system team.
    topology_type: str
    # Overarching guiding principle or long-term goal. Must be Clear, Inspiring, Quantifiable, Stakeholder Obsessed, and Unique.
    north_star: str
    # A mission statement that encapsulates the team's purpose and primary objectives
    mission: str
    # A vision statement that describes the future state the team aims to achieve
    vision: str
    # Short sentences that describe the team's values. Examples: 1) Security first, second, and last. 2) Make it work, make it right, make it fast. 3) Artifacts are king.
    values_principals: List[str]
    # Specific roles within the team, such as Team Lead, Developer, QA Engineer, etc., and their responsibilities. Do not include roles that do not have a clear purpose on the team.
    team_structure: List[TeamStructure]
    # Key stakeholders of this team's work
    stakeholders: Stakeholders
    # List prioritized deliverable goals. Priorities should follow the STAR format and be Specific, Tangible, Actionable, and Realistic.
    priorities: List[str]
    # List of specific channels hosted/created by this team to support their own team members or other teams using this team's services.
    communication_channels: List[CommunicationChannel]
    # Regular activities performed by this team to support internal planning, execution, operations, and direction-setting.
    routines: List[Routines]
    # The most important metrics that will objectively measure the performance of this team with leading indicators of success and risk. Must be readily measurable.
    performance_metrics: List[PerformanceMetric]
    # Services provided by this team to others. Could be deployed APIs, reusable libraries and modules, guides and documentation, or other services provided internally or externally.
    service_level_agreements: List[ServiceLevelAgreement]
    # Repositories of artifacts that are directly contributed to by this team.
    contributing_repositories: List[str]
    # Sources of knowledge for members of this team to onboard and find guides supporting them in their work.
    knowledge_bases: KnowledgeBase

# cloud_foundation_team = CloudFoundationTeam(**data)
