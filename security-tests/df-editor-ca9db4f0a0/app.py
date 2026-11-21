from flask import Flask, request, jsonify
        import subprocess

        app = Flask(__name__)

        @app.get("/greet")
        def greet():
            name = request.args.get("name", "guest")
            output = subprocess.check_output("echo Hello " + name, shell=True, text=True)
            return jsonify({"message": output})

        if __name__ == "__main__":
            app.run(host="0.0.0.0", port=8767)
        
