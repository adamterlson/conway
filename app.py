import os
import json
from flask import Flask, request, render_template
from openai import OpenAI
from agents.team_writer import SYSTEM_ROLE

client = OpenAI()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('start.html')

@app.route('/submit', methods=['POST'])
def submit():
    team_description = request.form['team_description']
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "JSON" },
            {"role": "system", "content": SYSTEM_ROLE },
            {"role": "user", "content": f"Team Description`{team_description}`" }
        ]
    )
    
    result = json.loads(completion.choices[0].message.content)
    print(json.dumps(result, indent=2))
    return render_template('start.html', **result)

if __name__ == '__main__':
    app.run(debug=True)
