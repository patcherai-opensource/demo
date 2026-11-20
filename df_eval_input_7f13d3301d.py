"""Isolated web endpoint fixture for security-review assessment."""
from flask import Flask, request

app = Flask(__name__)


@app.get("/test-evaluate")
def evaluate():
    expression = request.args["expression"]
    return str(eval(expression))
