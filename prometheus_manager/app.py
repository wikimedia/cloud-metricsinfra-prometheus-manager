import os

import flask
import yaml

from prometheus_manager.blueprints.v1.projects import projects
from prometheus_manager.config import construct_config
from prometheus_manager.database import alembic, database
from prometheus_manager.metrics import metrics


def create_app(db_account='USER'):
    app = flask.Flask(__name__)

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

    app.register_blueprint(projects)

    return app
