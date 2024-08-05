import os
import json
from flask import Flask, request, render_template
from openai import OpenAI
from agents.team_writer import SYSTEM_ROLE
from flask_caching import Cache
import hashlib

client = OpenAI()

app = Flask(__name__)

# Configure Flask-Caching
app.config['CACHE_TYPE'] = 'SimpleCache'  # Simple in-memory cache for demonstration
cache = Cache(app)

def generate_hash(data):
    """Generate a hash for the given data."""
    data_string = json.dumps(data, sort_keys=True)
    return hashlib.md5(data_string.encode('utf-8')).hexdigest()

def cached_completion(prompt):
    data_hash = generate_hash(prompt)
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
            {"role": "system", "content": SYSTEM_ROLE },
            {"role": "user", "content": f"Team Description`{prompt}`" }
        ]
    )

    response = completion.choices[0].message.content
    cache.set(data_hash, response, timeout=30000)
    print(response)
    
    return json.loads(response)

@app.route('/')
def index():
    return render_template('start.html')

@app.route('/submit', methods=['POST'])
def submit():
    team_description = request.form['team_description']
    data_hash = generate_hash(team_description)

    result = cached_completion(team_description)
    print(json.dumps(result, indent=2))
    return render_template('start.html', **result)

if __name__ == '__main__':
    app.run(debug=True)
