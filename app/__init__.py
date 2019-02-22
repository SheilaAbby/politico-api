from flask import Flask
from app.api.V1.views import app_route
from flask_jwt_extended import (JWTManager)
from instance.config import app_config
#  local imports
from os import environ


def create_app(config_name):  # creating the application in a function
    """
    creates the app
    :return:
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.secret_key = environ.get('SECRET_KEY')

    # Initialize JWT
    jwt = JWTManager(app)

    @jwt.token_in_blacklist_loader
    def check_blacklisted(token):
        from app.api.V1.models import RevokedTokenModel
        jti = token['jti']
        return RevokedTokenModel().is_blacklisted(jti)
    app.register_blueprint(app_route)

    return app
