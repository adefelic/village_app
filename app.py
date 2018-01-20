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
    if (request.args) :
    	with open('task.json', 'r+') as f:
    		tasks = json.load(f)
    		json.dumps(
    			{"id": "todo"},
    			{"description": request.args.get("description")},
    			)
        # load task, group, date, user
        # new task {	
        # "tasks": [
		# {
		#	"id": "" # bottom task id - "t_",  + 1 
		# 	"description": "pick up my kid",
		# 	"group": request.args.get("group")
		# 	"created_by": request.args.get("user")
		# 	"helper": "",
		# 	"when": request.args.get("when") -> to unix time
		# 	"expires": the above, + 2 hours
		# },}
        # 
        # update tasks list in group obj
        #
        # update tasks list in user obj
        #
    tasks = _get_json('task.json')
    users = _get_json('users.json')
    groups = _get_json('groups.json')
    return render_template('help-me.html', tasks=tasks,users=users,groups=groups)

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
