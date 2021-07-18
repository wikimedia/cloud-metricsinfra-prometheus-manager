from sqlalchemy import Column, Integer, String

from prometheus_manager.database import database


class Project(database.Model):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    openstack_id = Column(String(255), nullable=False, unique=True)
    name = Column(String(255), nullable=False, unique=True)
