import json
from flask import Blueprint, render_template, request, jsonify, current_app
from agents.north_star_grader import SYSTEM_ROLE as GRADER_SYSTEM_ROLE

grade_bp = Blueprint('grade', __name__)

def cached_grader_completion(prompt):
    completion = current_app.client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "JSON" },
            {"role": "system", "content": GRADER_SYSTEM_ROLE },
            {"role": "user", "content": f"User North Star`{prompt}`" }
        ]
    )

    response = completion.choices[0].message.content
    return json.loads(response)

@grade_bp.route('/', methods=['POST'])
def grade():
    data = request.get_json()
    print("GRADING")
    print(data)
    result = cached_grader_completion(data)
    resultHtml = render_template('grade.html', **result)
    return jsonify({'result': resultHtml})
