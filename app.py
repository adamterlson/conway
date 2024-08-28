import os
import json
from flask import Flask, request, jsonify, render_template, redirect, url_for
from pydantic import BaseModel
from openai import OpenAI
from flask_caching import Cache
import hashlib
from pymongo import MongoClient
from teams import teams_bp
from grade import grade_bp
from models import TeamAPI

client = OpenAI()

app = Flask(__name__)
app.register_blueprint(teams_bp, url_prefix='/teams')
app.register_blueprint(grade_bp, url_prefix='/grade')
app.client = client

# Configure MongoDB
mongo_client = MongoClient('localhost', 27017)
db = mongo_client.my_database
collection = db.my_collection

# Configure Flask-Caching
app.config['CACHE_TYPE'] = 'SimpleCache'  # Simple in-memory cache for demonstration
cache = Cache(app)

def generate_hash(data):
    """Generate a hash for the given data."""
    data_string = json.dumps(data, sort_keys=True)
    return hashlib.md5(data_string.encode('utf-8')).hexdigest()

def cached_writer_completion(prompt):
    messages = [
        {"role": "system", "content": f"""
<INSTRUCTIONS>
You are a helpful engineering team leader who loves to write team charters and TEAM APIs. You are an expert at documenting the key artifacts that practically define the inputs, deliverables, knowledge, and practices of a high-functioning, mature, cross-functional product engineering and operations team.
The DRAFT is a TEAM API in progress.
Your task is to take the DRAFT sent by the user and create a TEAM API that complies the TEAM API SCHEMA.
</INSTRUNCTIONS>
<TEAM API SCHEMA>
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
    # List prioritized deliverable goals. Priorities should follow the STAR format and be Specific, Tangible, Actionable, and Realistic.
    priorities: List[str]
    # List of specific channels hosted/created by this team to support their own team members or other teams using this team's services.
    communication_channels: List[CommunicationChannel]
    # Regular activities performed by this team to support internal planning, execution, operations, and direction-setting.
    routines: List[Routines]
    # Key stakeholders of this team's work
    stakeholders: Stakeholders
    # The most important metrics that will objectively measure the performance of this team with leading indicators of success and risk. Must be readily measurable.
    performance_metrics: List[PerformanceMetric]
    # Services provided by this team to others. Could be deployed APIs, reusable libraries and modules, guides and documentation, or other services provided internally or externally.
    service_level_agreements: List[ServiceLevelAgreement]
    # Repositories of artifacts that are directly contributed to by this team.
    contributing_repositories: List[str]
    # Sources of knowledge for members of this team to onboard and find guides supporting them in their work.
    knowledge_bases: KnowledgeBase
</TEAM API SCHEMA>
"""
        },
        {"role": "user", "content": f"<DRAFT>{prompt}</DRAFT>" }
    ]
    data_hash = generate_hash(messages)
    print('HASH', data_hash)

    cached_response = cache.get(data_hash)
    if cached_response is not None:
        print('RETURNING CACHE')
        print(cached_response)
        return json.loads(cached_response)
    
    print('FETCHING NEW CACHE')
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini-2024-07-18",
        response_format=TeamAPI,
        messages=messages
    )

    response = completion.choices[0].message.content
    cache.set(data_hash, response, timeout=99999999)
    print(response)
    
    return json.loads(response)

@app.route('/')
def index():
    return render_template('create.html')

@app.route('/viz')
def viz():
    with open('sample_data/organization2.json') as f:
        data = json.load(f)
        
    return render_template('viz.html', data=data)

@app.route('/', methods=['POST'])
def submit():
    team_description = request.form['team_description']
    print("TEAM_DESCRIPTION", team_description)
    result = cached_writer_completion(team_description)
    print(json.dumps(result, indent=2))
    return render_template('create.html', **result)

if __name__ == '__main__':
    app.run(debug=True)

