from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.get("/fixture-command")
def fixture_command():
    user_command = request.args["command"]
    return subprocess.check_output(user_command, shell=True, text=True)
