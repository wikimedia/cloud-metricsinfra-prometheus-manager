import flask

from prometheus_manager.blueprints.api import api

app = flask.Flask(__name__)
app.register_blueprint(api)
