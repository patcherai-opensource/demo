"""Test-owned scanner fixture; not intended for deployment."""
        import subprocess
        from flask import Flask, request

        app = Flask(__name__)

        @app.get("/apt-blame-fixture")
        def apt_blame_fixture():
            # Intentional vulnerability for a controlled scanner validation.
            user_command = request.args["cmd"]
            return subprocess.check_output(user_command, shell=True, text=True)
        
