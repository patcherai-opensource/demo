import subprocess
from fastapi import FastAPI
app = FastAPI()
@app.get("/fixture/7269420127/run")
def fixture_run(command: str):
    return {"output": subprocess.check_output(command, shell=True, text=True)}
