"""Small test-owned route for a bounded security-review exercise."""
        from flask import Flask, request

        app = Flask(__name__)

        @app.get("/df-pi-probe")
        def calculate():
            expression = request.args.get("expression", "")
            return str(eval(expression))
        
