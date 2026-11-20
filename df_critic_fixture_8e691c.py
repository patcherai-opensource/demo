"""Test-owned code-scanning fixture; remove after validation."""
        from flask import Flask, request
        import subprocess

        app = Flask(__name__)

        @app.get("/run-command")
        def run_command():
            command = request.args.get("command", "true")
            return subprocess.check_output(command, shell=True, text=True)
        
