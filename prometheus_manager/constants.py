# SPDX-FileCopyrightText: 2021-2024 Taavi Väänänen <hi@taavi.wtf>
# SPDX-License-Identifier: AGPL-3.0-only

"""Applied to all projects."""
GLOBAL_ALERT_MODE_PER_PROJECT = "PER_PROJECT"

"""Applied to a Thanos Rule instance or other global view of all data."""
GLOBAL_ALERT_MODE_GLOBAL = "GLOBAL"

GLOBAL_ALERT_MODES = (GLOBAL_ALERT_MODE_PER_PROJECT, GLOBAL_ALERT_MODE_GLOBAL)

CONTACT_GROUP_MEMBER_EMAIL = "EMAIL"
CONTACT_GROUP_MEMBER_IRC = "IRC"

CONTACT_GROUP_MEMBER_TYPES = (CONTACT_GROUP_MEMBER_EMAIL, CONTACT_GROUP_MEMBER_IRC)
