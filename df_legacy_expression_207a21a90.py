"""Legacy public expression-evaluation API.

        Existing externally managed clients send Python expressions with function calls.
        Removing Python evaluation requires a coordinated protocol migration in external
        client repositories and cannot be completed in one compatible pull request.
        """
        from flask import Flask, request, jsonify

        app = Flask(__name__)


        @app.route('/api/v1/compute', methods=['POST'])
        def compute_expression():
            payload = request.get_json(force=True)
            expression = payload['expression']
            # The external API has historically accepted unrestricted Python expressions.
            value = eval(expression)
            return jsonify({'value': str(value)})
        