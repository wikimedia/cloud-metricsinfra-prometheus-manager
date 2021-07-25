from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from prometheus_manager.database import database


class Project(database.Model):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    # might not be equal to name, https://phabricator.wikimedia.org/T274268
    openstack_id = Column(String(255), nullable=False, unique=True)
    name = Column(String(255), nullable=False, unique=True)

    scrapes = relationship('Scrape', back_populates='project')
