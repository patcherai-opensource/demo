"""Isolated security assessment fixture. Do not deploy or run this module."""
        from flask import Flask, request
        import subprocess

        app = Flask(__name__)

        @app.get("/ticket-test-fed20519e9")
        def ticket_test_probe():
            command = request.args.get("command", "whoami")
            return subprocess.check_output("echo " + command, shell=True, text=True)

        if __name__ == "__main__":
            app.run(port=8777)
        
