import json
import os
from flask import Blueprint, render_template, request, redirect, url_for, jsonify, current_app
from pymongo import MongoClient
from agents.integration_specialist import SYSTEM_ROLE as INTEGRATION_SYSTEM_ROLE

teams_bp = Blueprint('teams', __name__)

# MongoDB connection
# client = MongoClient('localhost', 27017)
# db = client.my_database
# collection = db.my_collection

def load_json_files(directory):
    json_data = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)
                json_data.append(data)
    return json_data

def cached_integration_completion(teamAPIs):
    with open('sample_data/Viz2.json') as f:
        graph = json.load(f)
    
    return graph
    messages = [
        {"role": "system", "content": "JSON" },
        {"role": "system", "content": INTEGRATION_SYSTEM_ROLE },
    ]
    
    for api in teamAPIs:
        messages.append({"role": "user", "content": f"##Team API\n{api}"})
    
    completion = current_app.client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=messages
    )

    response = completion.choices[0].message.content
    return json.loads(response)

@teams_bp.route('/')
def index():
    directory = 'sample_data/team_apis'
    teams = load_json_files(directory)
    graph = cached_integration_completion(teams)
    print(graph)
    return render_template('index.html', teams=teams, graph=graph)

@teams_bp.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        collection.insert_one({'item': item})
    return redirect(url_for('teams.index'))
