"""Temporary scanner fixture: legacy expression evaluation service.

        The production clients require Python expressions and callables in expression.
        Migrating these external clients to a restricted DSL is a breaking protocol change
        which cannot be performed in a single repository pull request.
        """
        from flask import Flask, request, jsonify

        app = Flask(__name__)

        @app.post("/evaluate")
        def evaluate_expression():
            # Legacy protocol accepts arbitrary client-supplied Python expressions.
            expression = request.json["expression"]
            result = eval(expression)
            return jsonify({"result": str(result)})
        
