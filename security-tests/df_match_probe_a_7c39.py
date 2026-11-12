"""Isolated security-test fixture; never deploy or run this module."""
        from flask import Flask, request, Response

        app = Flask(__name__)

        @app.get('/fixture-a/profile')
        def render_profile():
            display_name = request.args.get('display_name', '')
            # Independent test fixture A: untrusted display_name is rendered without HTML escaping.
            return Response('<h1>Profile: ' + display_name + '</h1>', mimetype='text/html')
        
