"""Isolated security scanner test fixture; not included in any deployed app."""
  from flask import Flask, request
  import subprocess

  app = Flask(__name__)

  @app.get('/resolution-fixture/alpha')
  def alpha_report():
      command = request.args.get('command', '')
      return subprocess.check_output(command, shell=True, text=True)
  
