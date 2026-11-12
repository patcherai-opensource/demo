"""Isolated security-test fixture; never deploy or run this module."""
        from flask import Flask, request, Response

        app = Flask(__name__)

        @app.get('/fixture-b/invoice')
        def render_invoice():
            invoice_label = request.args.get('invoice_label', '')
            # Independent test fixture B: untrusted invoice_label is rendered without HTML escaping.
            return Response('<h1>Invoice: ' + invoice_label + '</h1>', mimetype='text/html')
        
