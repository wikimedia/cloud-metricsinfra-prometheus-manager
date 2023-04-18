from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy_json import MutableJson

from prometheus_manager.database import database


class Project(database.Model):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    # might not be equal to name, https://phabricator.wikimedia.org/T274268
    openstack_id = Column(String(255), nullable=False, unique=True)
    name = Column(String(255), nullable=False, unique=True)
    extra_labels = Column(MutableJson, nullable=False)

    default_contact_group_id = Column(
        Integer, ForeignKey('contact_groups.id', ondelete='SET NULL'), nullable=True
    )

    acl_group = Column(String(255), nullable=True)

    alerts = relationship('AlertRule', back_populates='project')
    scrapes = relationship('Scrape', back_populates='project')
    contact_groups = relationship(
        'ContactGroup', back_populates='project', foreign_keys='ContactGroup.project_id'
    )
    default_contact_group = relationship(
        'ContactGroup', uselist=False, foreign_keys='Project.default_contact_group_id'
    )
