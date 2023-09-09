# flake8: noqa: F401
from prometheus_manager.models.alert import AlertRule, BaseAlertRule, GlobalAlertRule
from prometheus_manager.models.notifications import ContactGroup, ContactGroupMember
from prometheus_manager.models.project import Project
from prometheus_manager.models.scrape import (
    BlackboxHttpConfig,
    OpenstackDiscovery,
    OpenstackSupportedImage,
    Scrape,
    StaticDiscovery,
)
