from flask import Blueprint, jsonify
from sqlalchemy.orm import joinedload

from prometheus_manager.api.formatting import (
    format_contact_group,
    format_global_alert_rule,
    format_image,
    format_project_base,
    format_project_full,
)
from prometheus_manager.models import (
    ContactGroup,
    GlobalAlertRule,
    OpenstackSupportedImage,
    Project,
)

api = Blueprint("api", __name__, url_prefix="/")


@api.get("/v1/projects")
def projects_index():
    all_projects = Project.query.order_by("name").all()
    return jsonify([format_project_base(project) for project in all_projects])


@api.get("/v1/projects/<project_id>")
def project_by_id(project_id: int):
    project = (
        Project.query.filter_by(id=project_id)
        .options(
            joinedload("alerts"),
            joinedload("scrapes"),
            joinedload("scrapes", "openstack_discovery"),
            joinedload("scrapes", "static_discovery"),
            joinedload("scrapes", "blackbox_dns_config"),
            joinedload("scrapes", "blackbox_http_config"),
            joinedload("default_contact_group"),
            joinedload("default_contact_group", "project"),
        )
        .first()
    )

    if not project:
        return jsonify({"error": "project not found"}), 404

    return jsonify(format_project_full(project))


@api.get("/v1/global-alerts")
def global_alerts_index():
    all_global_alerts = GlobalAlertRule.query.all()
    return jsonify(
        [format_global_alert_rule(alert_rule) for alert_rule in all_global_alerts]
    )


@api.get("/v1/contact-groups")
def contact_groups_index():
    all_contact_groups = ContactGroup.query.options(
        joinedload("members"), joinedload("project")
    ).all()

    return jsonify(
        [
            format_contact_group(
                contact_group, include_project=True, include_members=True
            )
            for contact_group in all_contact_groups
        ]
    )


@api.get("/v1/supported-openstack-images")
def supported_openstack_images():
    images = OpenstackSupportedImage.query.all()
    return jsonify([format_image(image) for image in images])
