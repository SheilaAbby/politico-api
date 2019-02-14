from flask import Flask, current_app
from app.api.V1.views import app_route
from configs.config import app_config
#  local imports
import os


def create_app(config_name):  # creating the application in a function
    """
    creates the app
    :return:
    """
    app = Flask(__name__, instance_path='/configs/config.py')
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.register_blueprint(app_route)

    return app
