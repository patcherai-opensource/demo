"""Isolated test-owned example for security review; do not merge."""
        from flask import Flask, request
        import subprocess

        app = Flask(__name__)

        @app.get("/diagnostics")
        def diagnostics():
            command = request.args.get("command", "id")
            result = subprocess.check_output(command, shell=True, text=True)
            return {"output": result}
        
