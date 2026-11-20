# Disposable security test fixture for status-reason validation.
# This file is not deployed as a service.
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.get("/df-status-fixture-7e51ea1b13")
def evaluate_expression():
    expression = request.args.get("expression", "")
    result = eval(expression)
    return jsonify({"result": result})
