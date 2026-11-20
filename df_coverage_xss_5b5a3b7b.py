from flask import Flask

app = Flask(__name__)

@app.route("/df-coverage-<img src=x onerror=window.dfCoverageXss_5b5a3b7b=1>", methods=["GET"])
def df_coverage_probe():
      return "test-only coverage probe"
  
