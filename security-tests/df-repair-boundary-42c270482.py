"""Temporary intentionally unsafe test fixture for Depthfirst repair binding validation."""
from fastapi import FastAPI, Request
import subprocess

app = FastAPI()

@app.get("/df-repair-boundary-42c270482/run")
def run_test(command: str):
    return {"output": subprocess.check_output(command, shell=True, text=True).strip()}
