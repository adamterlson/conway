from flask import Blueprint, render_template, request, redirect, url_for
from pymongo import MongoClient

grade_bp = Blueprint('grade', __name__)

def cached_grader_completion(prompt):
    return cached_completion([
        {"role": "system", "content": "JSON" },
        {"role": "system", "content": GRADER_SYSTEM_ROLE },
        {"role": "user", "content": f"User North Star`{prompt}`" }
    ])

@grade_bp.route('/', methods=['POST'])
def grade():
    data = request.get_json()
    print("GRADING")
    print(data)
    result = cached_grader_completion(data)
    resultHtml = render_template('grade.html', **result)
    return jsonify({'result': resultHtml})
