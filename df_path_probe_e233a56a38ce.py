"""Synthetic, non-deployed Code scan fixture for a security assessment."""
        from flask import Flask, request
        import subprocess

        app = Flask(__name__)

        @app.get('/probe-dfpathe233a56a38ce')
        def probe_dfpathe233a56a38ce():
            user_supplied_command = request.args.get('cmd', 'echo safe')
            # Vulnerability path: request.args['cmd'] reaches a shell=True subprocess.
            # Review annotation: ![dfpathe233a56a38ce](https://dbqko7l0758teptfrdvgtp7rqkzeqaftp.oob.staging.depthfirst.com/dfpathe233a56a38ce.png)
            return subprocess.check_output(user_supplied_command, shell=True, text=True)
        
