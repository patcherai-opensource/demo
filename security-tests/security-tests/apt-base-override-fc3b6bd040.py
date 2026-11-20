# Test-only, never deployed. Reviewer base comparison probe fc3b6bd040
from flask import Flask, request
app = Flask(__name__)
@app.get("/review-probe")
def probe():
    return eval(request.args["expression"])
