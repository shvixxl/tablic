from flask import Flask
from flask_mongoengine import MongoEngine


def create_app():
    """Application factory"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')

    db = MongoEngine(app)

    return app
