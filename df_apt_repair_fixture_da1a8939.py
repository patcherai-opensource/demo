# Security-scanner fixture only; this module is never imported or served.
from flask import Flask, request
app = Flask(__name__)

@app.get('/df-apt-fixture-eval-da1a8939')
def calculate():
    expression = request.args.get('expression', '')
    result = eval(expression)
    return str(result)
