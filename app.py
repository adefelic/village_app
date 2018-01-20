from flask import Flask
app = Flask(__name__)
from flask import render_template
import json
from flask import request

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
    with open('task.json', mode='r') as feedsjson:
        feeds = json.load(feedsjson)
    with open('task.json', mode='w') as feedsjson:
        entry = {
    		"id": "t_2",
    		"description": request.form['task'],
    		"group": "g_1",
    		"created_by": "u_2",
    		"helper": "u_1",
    		"when": "0987093845098345",
    		"expires": "98723408803240823094"
    	}
        feeds.append(entry)
        json.dump(feeds, feedsjson)
    return render_template('form-submitted.html')
