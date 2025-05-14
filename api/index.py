import os
from flask_app import create_app

os.environ["MPLCONFIGDIR"] = "/tmp"

app = create_app()

def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)
