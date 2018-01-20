from flask import Flask
app = Flask(__name__)
from flask import render_template
import json

def _get_json(path):
    with open(path) as json_data:
        json_data = json.loads(json_data.read())
        return json.dumps(json_data)

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
    tasks = _get_json('task.json')
    users = _get_json('users.json')
    groups = _get_json('groups.json')
    return render_template(
        'tasks.html',
        tasks=tasks,
        users=users,
        groups=groups,
    )

@app.route("/create/task/", methods=['POST'])
def create_task():
    import ipdb; ipdb.set_trace()
    print(request.form)
