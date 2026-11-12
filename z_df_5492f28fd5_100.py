from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.get("/list-user-directory")
def list_user_directory():
    return subprocess.check_output("ls " + request.args["path"], shell=True).decode()
