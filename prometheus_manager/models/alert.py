from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy_json import MutableJson

from prometheus_manager.database import database


class AlertRule(database.Model):
    __tablename__ = 'alerts'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id', ondelete='CASCADE'), nullable=False)
    name = Column(String(255), nullable=False)

    query = Column(String(2048))
    duration = Column(String(32), nullable=False, server_default='1m')

    severity = Column(String(32), nullable=False, server_default='warn')
    annotations = Column(MutableJson, nullable=False)

    project = relationship('Project', back_populates='alerts', uselist=False)

    __table_args__ = (UniqueConstraint('project_id', 'name', name='u_project_name'),)
