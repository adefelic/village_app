from flask import Flask
app = Flask(__name__)
from flask import render_template
import json

def _get_json(path):
    with open(path) as json_data:
        return json.loads(json_data.read())

@app.route("/")
def index():
    tasks = _get_json('task.json')
    users = _get_json('users.json')
    groups = _get_json('groups.json')
    return render_template('index.html', tasks=tasks, users=users, groups=groups,)

@app.route("/groups/", methods=['GET'])
def groups():
    tasks = _get_json('task.json')
    users = _get_json('users.json')
    groups = _get_json('groups.json')
    return render_template('groups.html', tasks=tasks, users=users, groups=groups)

@app.route("/help-me/", methods=['GET'])
def help_me():
    tasks = _get_json('task.json')
    users = _get_json('users.json')
    groups = _get_json('groups.json')
    return render_template('help-me.html',tasks=tasks,users=users,groups=groups)

@app.route("/tasks/", methods=['GET'])
def tasks():
    return render_template(
        'tasks.html',
        tasks=tasks,
        users=users,
        groups=groups,
    )
