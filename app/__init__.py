from flask import Flask

#  local imports

from app.api.V1.views import app_route


def create_app():
    app = Flask(__name__)
    app.register_blueprint(app_route, url_prefix='/api/v1')
    return app
