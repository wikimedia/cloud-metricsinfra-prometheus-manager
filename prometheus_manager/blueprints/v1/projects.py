from flask import Blueprint, jsonify
from sqlalchemy.orm import joinedload

from prometheus_manager.models import Project

projects = Blueprint('v1projects', __name__, url_prefix='/v1/projects')


@projects.get('')
def projects_index():
    all_projects = Project.query.all()
    return jsonify(
        [
            {
                'id': project.id,
                'openstack_id': project.openstack_id,
                'name': project.name,
            }
            for project in all_projects
        ]
    )


@projects.get('/<project_id>')
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

    return jsonify(
        {
            'id': project.id,
            'openstack_id': project.openstack_id,
            'name': project.name,
            'alert_rules': [
                {
                    'id': alert.id,
                    'name': alert.name,
                    'query': alert.query,
                    'duration': alert.duration,
                    'severity': alert.severity,
                    'annotations': alert.annotations,
                }
                for alert in project.alerts
            ],
            'scrapes': [
                {
                    'id': scrape.id,
                    'name': scrape.name,
                    'path': scrape.path,
                    'openstack_discovery': {
                        'name_regex': scrape.openstack_discovery.name_regex,
                        'port': scrape.openstack_discovery.port,
                    }
                    if scrape.openstack_discovery
                    else None,
                }
                for scrape in project.scrapes
            ],
        }
    )
