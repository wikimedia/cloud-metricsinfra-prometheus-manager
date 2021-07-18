from flask import Blueprint, jsonify

from prometheus_manager.models import Project

projects = Blueprint('projectsv1', __name__, url_prefix='/projects/v1')


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
