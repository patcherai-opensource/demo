"""Test-owned security review fixture 884c3dcfe1. Not deployed."""
        from flask import Flask, request
        import subprocess

        app = Flask(__name__)

        @app.get("/probe/884c3dcfe1")
        def probe():
            address = request.args["address"]
            # Deliberately vulnerable fixture: untrusted address is interpolated into a shell command.
            return subprocess.check_output("nslookup " + address, shell=True, text=True)
        
