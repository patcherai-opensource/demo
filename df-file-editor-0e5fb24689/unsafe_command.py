"""Disposable source-scanner fixture. Not deployed or imported."""
        import subprocess
        from flask import Flask, request

        app = Flask(__name__)

        @app.get("/df-file-editor-0e5fb24689/run")
        def run_user_command():
            # Intentionally vulnerable fixture: untrusted HTTP parameter becomes a shell command.
            user_command = request.args["command"]
            return subprocess.check_output(user_command, shell=True, text=True)
        
