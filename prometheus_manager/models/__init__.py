# SPDX-FileCopyrightText: 2021-2024 Taavi Väänänen <hi@taavi.wtf>
# SPDX-License-Identifier: AGPL-3.0-only

# flake8: noqa: F401
from prometheus_manager.models.alert import AlertRule, BaseAlertRule, GlobalAlertRule
from prometheus_manager.models.notifications import ContactGroup, ContactGroupMember
from prometheus_manager.models.project import Project
from prometheus_manager.models.scrape import (
    BlackboxDnsConfig,
    BlackboxHttpConfig,
    OpenstackDiscovery,
    OpenstackSupportedImage,
    Scrape,
    StaticDiscovery,
)
