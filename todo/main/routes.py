from flask import Blueprint, render_template, request, url_for, redirect
from todo.extensions import mongo
from bson import ObjectId

main = Blueprint('main', __name__)


@main.route('/')
def index():
    todo_db = mongo.db.todo
    todos = todo_db.find()
    return render_template('index.html', todos=todos)


@main.route('/api/add', methods=['POST'])
def add():
    todo_db = mongo.db.todo
    todo_item = request.form.get('add-todo')
    todo_db.insert_one({'text': todo_item, 'complete': False})
    return redirect(url_for('main.index'))


@main.route('/api/update/<id>', methods=['GET'])
def update(id):
    todo_db = mongo.db.todo
    todo_item = todo_db.find_one({"_id": ObjectId(id)})
    todo_item['complete'] = True
    todo_db.update_one({"_id": ObjectId(id)}, {"$set": {'complete': True}})
    return redirect(url_for('main.index'))
