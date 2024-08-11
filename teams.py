from flask import Blueprint, render_template, request, redirect, url_for
from pymongo import MongoClient

teams_bp = Blueprint('teams', __name__)

# MongoDB connection
client = MongoClient('localhost', 27017)
db = client.my_database
collection = db.my_collection

@teams_bp.route('/')
def index():
    items = collection.find()
    return render_template('index.html', items=items)

@teams_bp.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        collection.insert_one({'item': item})
    return redirect(url_for('teams.index'))
