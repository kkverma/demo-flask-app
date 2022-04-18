from flask import Flask
from app.api.api import api

def createApp():
    app = Flask(__name__)
    app.register_blueprint(api)
    return app

