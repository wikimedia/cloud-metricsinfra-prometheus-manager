from prometheus_manager.models import (
    BaseAlertRule,
    ContactGroup,
    GlobalAlertRule,
    Project,
    Scrape,
)


def format_project_base(project: Project):
    return {
        'id': project.id,
        'openstack_id': project.openstack_id,
        'name': project.name,
    }


def format_alert_rule(alert: BaseAlertRule):
    return {
        'id': alert.id,
        'name': alert.name,
        'expr': alert.expr,
        'query': alert.expr,  # backwards compat, until configurator has been updated
        'duration': alert.duration,
        'severity': alert.severity,
        'annotations': alert.annotations,
    }


def format_global_alert_rule(alert: GlobalAlertRule):
    base = format_alert_rule(alert)
    return {
        **base,
        'mode': alert.mode,
    }


def format_scrape(scrape: Scrape):
    return {
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


def format_project_full(project: Project):
    base = format_project_base(project)
    return {
        **base,
        'alert_rules': [format_alert_rule(alert) for alert in project.alerts],
        'scrapes': [format_scrape(scrape) for scrape in project.scrapes],
    }


def format_contact_group(
    contact_group: ContactGroup, include_project: bool = False, include_members: bool = False
) -> dict:
    data = {
        'id': contact_group.id,
        'name': contact_group.name,
        'project_id': contact_group.project_id,
    }

    if include_project:
        data['project'] = format_project_base(contact_group.project)
    if include_members:
        data['members'] = [
            {
                'id': member.id,
                'type': member.type,
                'value': member.value,
            }
            for member in contact_group.members
        ]

    return data
