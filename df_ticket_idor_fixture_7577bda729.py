"""Assessment-only security fixture 7577bda729; remove after testing."""
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/assessment/7577bda729/calculate")
def calculate():
    # Deliberately unsafe: attacker-supplied expression executes Python code.
    expression = request.args.get("expression", "0")
    result = eval(expression)
    return jsonify({"result": str(result)})
