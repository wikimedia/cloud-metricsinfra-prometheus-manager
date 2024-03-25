# SPDX-FileCopyrightText: 2021-2024 Taavi Väänänen <hi@taavi.wtf>
# SPDX-License-Identifier: AGPL-3.0-only

from prometheus_manager.models import (
    BaseAlertRule,
    ContactGroup,
    GlobalAlertRule,
    OpenstackSupportedImage,
    Project,
    Scrape,
)


def format_project_base(project: Project):
    return {
        "id": project.id,
        "openstack_id": project.openstack_id,
        "name": project.name,
        "extra_labels": project.extra_labels,
    }


def format_alert_rule(alert: BaseAlertRule):
    return {
        "id": alert.id,
        "name": alert.name,
        "expr": alert.expr,
        "query": alert.expr,  # backwards compat, until configurator has been updated
        "duration": alert.duration,
        "severity": alert.severity,
        "annotations": alert.annotations,
    }


def format_global_alert_rule(alert: GlobalAlertRule):
    base = format_alert_rule(alert)
    return {
        **base,
        "mode": alert.mode,
    }


def format_scrape(scrape: Scrape):
    blackbox = None
    if scrape.scheme in ("tcp", "udp") and scrape.blackbox_dns_config:
        blackbox = {
            "type": "dns",
            "query_name": scrape.blackbox_dns_config.query_name,
            "query_type": scrape.blackbox_dns_config.query_type,
            "require_answer_match": scrape.blackbox_dns_config.require_answer_match,
        }
    elif scrape.scheme in ("http", "https") and scrape.blackbox_http_config:
        blackbox = {
            "type": "http",
            "host": scrape.blackbox_http_config.host,
            "method": scrape.blackbox_http_config.method,
            "headers": scrape.blackbox_http_config.headers,
            "follow_redirects": scrape.blackbox_http_config.follow_redirects,
            "valid_status_codes": scrape.blackbox_http_config.valid_status_codes,
            "require_body_match": scrape.blackbox_http_config.require_body_match,
            "require_body_not_match": scrape.blackbox_http_config.require_body_not_match,
        }

    return {
        "id": scrape.id,
        "name": scrape.name,
        "scheme": scrape.scheme,
        "path": scrape.path,
        "blackbox": blackbox,
        "openstack_discovery": (
            {
                "name_regex": scrape.openstack_discovery.name_regex,
                "port": scrape.openstack_discovery.port,
            }
            if scrape.openstack_discovery
            else None
        ),
        "static_discovery": [
            {
                "host": target.host,
                "port": target.port,
            }
            for target in scrape.static_discovery
        ],
    }


def format_project_full(project: Project):
    base = format_project_base(project)
    return {
        **base,
        "acl_group": project.acl_group,
        "default_contact_group": (
            format_contact_group(project.default_contact_group, include_project=True)
            if project.default_contact_group
            else None
        ),
        "alert_rules": [format_alert_rule(alert) for alert in project.alerts],
        "scrapes": [format_scrape(scrape) for scrape in project.scrapes],
    }


def format_contact_group(
    contact_group: ContactGroup,
    include_project: bool = False,
    include_members: bool = False,
) -> dict:
    data = {
        "id": contact_group.id,
        "name": contact_group.name,
        "project_id": contact_group.project_id,
    }

    if include_project:
        data["project"] = format_project_base(contact_group.project)
    if include_members:
        data["members"] = [
            {
                "id": member.id,
                "type": member.type,
                "value": member.value,
            }
            for member in contact_group.members
        ]

    return data


def format_image(image: OpenstackSupportedImage) -> dict:
    return {
        "openstack_id": image.openstack_id,
    }
