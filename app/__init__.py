from flask import Flask, current_app
from app.api.V1.views import app_route
from configs.config import app_config
#  local imports
import os


def create_app():  # creating the application in a function
    """
    creates the app
    :return:
    """
    app = Flask(__name__)
    app.register_blueprint(app_route)

    return app
