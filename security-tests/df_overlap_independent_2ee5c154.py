"""Security scanner test fixture; do not deploy or run this server."""
        from flask import Flask, request
        import subprocess

        app = Flask(__name__)

        @app.get("/probe")
        def probe():
            # Test-only vulnerable input-to-shell path. Never invoke the handler.
            result = subprocess.check_output(request.args["cmd"], shell=True, text=True)
            return result

        if __name__ == "__main__":
            app.run(host="0.0.0.0", port=8766)
        
