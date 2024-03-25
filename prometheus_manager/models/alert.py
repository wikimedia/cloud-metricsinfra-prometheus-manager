# SPDX-FileCopyrightText: 2021-2024 Taavi Väänänen <hi@taavi.wtf>
# SPDX-License-Identifier: AGPL-3.0-only

from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy_json import MutableJson

from prometheus_manager.constants import (
    GLOBAL_ALERT_MODE_PER_PROJECT,
    GLOBAL_ALERT_MODES,
)
from prometheus_manager.database import database


class BaseAlertRule:
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    expr = Column(String(2048), nullable=False)
    duration = Column(String(32), nullable=False, server_default="1m")

    severity = Column(String(32), nullable=False, server_default="warn")
    annotations = Column(MutableJson, nullable=False)


class AlertRule(BaseAlertRule, database.Model):
    __tablename__ = "alerts"

    project_id = Column(
        Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False
    )

    project = relationship("Project", back_populates="alerts", uselist=False)


class GlobalAlertRule(BaseAlertRule, database.Model):
    __tablename__ = "global_alerts"

    mode = Column(
        Enum(*GLOBAL_ALERT_MODES),
        nullable=False,
        server_default=GLOBAL_ALERT_MODE_PER_PROJECT,
    )
