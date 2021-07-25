from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from prometheus_manager.database import database


class Scrape(database.Model):
    __tablename__ = 'scrapes'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id', ondelete='CASCADE'), nullable=False)
    name = Column(String(255), nullable=False)

    project = relationship('Project', back_populates='scrapes', uselist=False)
    openstack_discovery = relationship(
        'OpenstackDiscovery', back_populates='scrape', uselist=False
    )

    __table_args__ = (UniqueConstraint('project_id', 'name', name='u_project_name'),)


class OpenstackDiscovery(database.Model):
    __tablename__ = 'scrape_discovery_openstack'
    id = Column(Integer, primary_key=True)
    scrape_id = Column(Integer, ForeignKey('scrapes.id', ondelete='CASCADE'), unique=True)
    port = Column(Integer, nullable=False)
    name_regex = Column(String(1023), nullable=True)

    scrape = relationship('Scrape', back_populates='openstack_discovery', uselist=False)
