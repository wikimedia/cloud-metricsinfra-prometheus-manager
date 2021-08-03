from flask import Blueprint, jsonify
from sqlalchemy.orm import joinedload

from prometheus_manager.api.formatting import (
    format_global_alert_rule,
    format_project_base,
    format_project_full,
)
from prometheus_manager.models import Project
from prometheus_manager.models.alert import GlobalAlertRule

api = Blueprint('api', __name__, url_prefix='/')


@api.get('/v1/projects')
def projects_index():
    all_projects = Project.query.all()
    return jsonify([format_project_base(project) for project in all_projects])


@api.get('/v1/projects/<project_id>')
def project_by_id(project_id: int):
    project = (
        Project.query.filter_by(id=project_id)
        .options(
            joinedload('alerts'),
            joinedload('scrapes'),
            joinedload('scrapes', 'openstack_discovery'),
        )
        .first()
    )

    if not project:
        return jsonify({'error': 'project not found'}), 404

    return jsonify(format_project_full(project))


@api.get('/v1/global-alerts')
def global_alerts_index():
    all_global_alerts = GlobalAlertRule.query.all()
    return jsonify([format_global_alert_rule(alert_rule) for alert_rule in all_global_alerts])