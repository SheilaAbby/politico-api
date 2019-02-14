from flask import Flask, current_app
from app.api.V1.views import app_route

#  local imports


def create_app():
    app = Flask(__name__)
    with app.app_context():
        app.register_blueprint(app_route, url_prefix='/api/v1')

    return app
