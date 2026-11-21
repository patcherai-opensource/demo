from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.get("/diagnostic")
def diagnostic():
    host = request.args["host"]
    return subprocess.check_output("ping -c 1 " + host, shell=True, text=True)

@app.post("/evaluate")
def evaluate_expression():
    expression = request.get_json()["expression"]
    return str(eval(expression))
