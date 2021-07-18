import flask

from prometheus_manager.blueprints.api import api
from prometheus_manager.metrics import metrics


def create_app():
    app = flask.Flask(__name__)
    metrics.init_app(app)

    app.register_blueprint(api)
    return app
