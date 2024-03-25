# SPDX-FileCopyrightText: 2021-2024 Taavi Väänänen <hi@taavi.wtf>
# SPDX-License-Identifier: AGPL-3.0-only

from sqlalchemy import Column, Enum, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from prometheus_manager.constants import CONTACT_GROUP_MEMBER_TYPES
from prometheus_manager.database import database


class ContactGroup(database.Model):
    __tablename__ = "contact_groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    project_id = Column(
        Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False
    )

    project = relationship(
        "Project",
        back_populates="contact_groups",
        foreign_keys="ContactGroup.project_id",
        uselist=False,
    )
    members = relationship("ContactGroupMember", back_populates="contact_group")

    __table_args__ = (UniqueConstraint("project_id", "name", name="u_project_name"),)


class ContactGroupMember(database.Model):
    __tablename__ = "contact_group_members"

    id = Column(Integer, primary_key=True)
    contact_group_id = Column(
        Integer, ForeignKey("contact_groups.id", ondelete="CASCADE"), nullable=False
    )

    type = Column(Enum(*CONTACT_GROUP_MEMBER_TYPES), nullable=False)
    value = Column(String(1024), nullable=False)

    contact_group = relationship(
        "ContactGroup", back_populates="members", uselist=False
    )
