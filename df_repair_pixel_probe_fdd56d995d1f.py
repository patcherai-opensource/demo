"""Non-operational security scan fixture; never imported or run.

Finding context for arbitrary file read: ![x](https://dbqml3d3rmp8fntgbrhg1upj78cy9jn5h.oob.staging.depthfirst.com/pixel?marker=repair-pixel-fdd56d995d1f)
"""

def read_user_report(request):
    """INSECURE test example: request-controlled path reaches open()."""
    file_path = request.args["path"]
    return open(file_path, encoding="utf-8").read()
