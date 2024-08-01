import os
import json
from flask import Flask, request, render_template
from openai import OpenAI
client = OpenAI()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    prompt = f"Return JSON. Is this likely a man, woman, or helicopter? First name: {first_name}, Last name: {last_name}. ```gender: the gender ```"
    
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": prompt }
        ]
    )
    
    result = json.dumps(json.loads(completion.choices[0].message.content), indent=2)
    
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
