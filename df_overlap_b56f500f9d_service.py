import subprocess
from fastapi import FastAPI

app = FastAPI()

@app.get("/audit/first")
def audit_first(command: str):
    output = subprocess.check_output(command, shell=True, text=True)
    return {"output": output}
