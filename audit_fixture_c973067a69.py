from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.get("/admin/backup")
def backup():
    path = request.args.get("path", "/var/log/app")
    subprocess.run("tar -czf /tmp/backup.tar.gz " + path, shell=True, check=True)
    return "Backup complete"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
