from flask import Flask, request, jsonify; app = Flask(__name__); app.add_url_rule("/evaluate", "evaluate", lambda: jsonify({"result": str(eval(request.get_json()["expression"]))}), methods=["POST"])
