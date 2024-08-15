import os
import json
from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from flask_caching import Cache
from agents.team_writer import SYSTEM_ROLE as WRITER_SYSTEM_ROLE
import hashlib
from pymongo import MongoClient
from teams import teams_bp
from grade import grade_bp



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

def cached_completion(messages):
    data_hash = generate_hash(messages)
    print('HASH', data_hash)

    cached_response = cache.get(data_hash)
    if cached_response is not None:
        print('RETURNING CACHE')
        print(cached_response)
        return json.loads(cached_response)
    
    print('FETCHING NEW CACHE')
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "JSON" },
            *messages,
        ]
    )

    response = completion.choices[0].message.content
    cache.set(data_hash, response, timeout=99999999)
    print(response)
    
    return json.loads(response)

def cached_writer_completion(prompt):
    return cached_completion([
        {"role": "system", "content": WRITER_SYSTEM_ROLE },
        {"role": "user", "content": f"Team Description`{prompt}`" }
    ])

@app.route('/')
def index():
    return render_template('start.html')

@app.route('/viz')
def viz():
    with open('sample_data/organization2.json') as f:
        data = json.load(f)
    return render_template('viz.html', data=data)

@app.route('/submit', methods=['POST'])
def submit():
    team_description = request.form['team_description']
    print("TEAM_DESCRIPTION", team_description)
    result = cached_writer_completion(team_description)
    print(json.dumps(result, indent=2))
    return render_template('start.html', **result)

if __name__ == '__main__':
    app.run(debug=True)
