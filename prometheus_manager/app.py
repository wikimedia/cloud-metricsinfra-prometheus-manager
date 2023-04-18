import os

import flask
import yaml

from prometheus_manager.api.blueprint import api
from prometheus_manager.config import construct_config
from prometheus_manager.database import alembic, database
from prometheus_manager.metrics import metrics


def create_app(db_account='USER'):
    app = flask.Flask(__name__)

    if not os.environ.get('PROMETHEUS_MANAGER_CONFIG_PATH'):
        raise Exception('No PROMETHEUS_MANAGER_CONFIG_PATH env var found, make sure to set it.')

    for config_file in os.environ.get('PROMETHEUS_MANAGER_CONFIG_PATH').split(','):
        with open(config_file, 'r') as file:
            app.config.update(yaml.safe_load(file))

    with app.app_context():
        construct_config(db_account)

    database.init_app(app)
    alembic.init_app(app)

    metrics.init_app(app)
    with app.app_context():
        metrics.register_endpoint('/metrics')

    app.register_blueprint(api)

    return app
