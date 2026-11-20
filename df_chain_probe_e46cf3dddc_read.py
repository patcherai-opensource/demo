from flask import Flask, request, send_file
app = Flask(__name__)

@app.get("/probe/read")
def read_report():
    return send_file(request.args["path"])
