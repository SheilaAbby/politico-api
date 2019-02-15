from flask import Flask
from app.api.V1.views import app_route
from configs.config import app_config
#  local imports
import os


def create_app(config_name):  # creating the application in a function
    """
    creates the app
    :return:
    """
    app = Flask(__name__)
    app.register_blueprint(app_route)

    return app
