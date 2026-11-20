# Test-owned security scanner fixture; delete after validation.
import os
from flask import Flask, request
app = Flask(__name__)
@app.route("/apt_status_idor_b28b2d6b", methods=["POST"])
def dangerous():
    user_input = request.form["code"]
    return str(eval(user_input))
