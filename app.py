from flask import Flask
app = Flask(__name__)
from flask import render_template
import json

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/groups/", methods=['GET'])
def groups():
    return render_template('groups.html')

@app.route("/help-me/", methods=['GET'])
def help_me():
    return render_template('help-me.html')

@app.route("/tasks/", methods=['GET'])
def tasks():
    return render_template('tasks.html')
