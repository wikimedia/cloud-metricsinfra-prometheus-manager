from sqlalchemy import (
    Boolean,
    Column,
    Enum,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship
from sqlalchemy_json import NestedMutableJson

from prometheus_manager.database import database


class OpenstackSupportedImage(database.Model):
    __tablename__ = "openstack_supported_images"
    id = Column(Integer, primary_key=True)
    openstack_id = Column(String(36), nullable=False, unique=True)


class Scrape(database.Model):
    __tablename__ = "scrapes"
    id = Column(Integer, primary_key=True)
    project_id = Column(
        Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False
    )
    name = Column(String(255), nullable=False)

    scheme = Column(Enum("http", "https"), nullable=False, server_default="http")
    path = Column(String(255), nullable=False, server_default="/metrics")

    project = relationship("Project", back_populates="scrapes", uselist=False)
    blackbox_http_config = relationship(
        "BlackboxHttpConfig", back_populates="scrape", uselist=False
    )
    openstack_discovery = relationship(
        "OpenstackDiscovery", back_populates="scrape", uselist=False
    )
    static_discovery = relationship(
        "StaticDiscovery", back_populates="scrape", uselist=True
    )

    __table_args__ = (UniqueConstraint("project_id", "name", name="u_project_name"),)


class BlackboxHttpConfig(database.Model):
    __tablename__ = "scrape_blackbox_http"
    id = Column(Integer, primary_key=True)
    scrape_id = Column(
        Integer, ForeignKey("scrapes.id", ondelete="CASCADE"), unique=True
    )

    host = Column(String(255), nullable=True)
    method = Column(String(255), nullable=False)
    headers = Column(NestedMutableJson, nullable=True)
    follow_redirects = Column(Boolean, nullable=False, default=False)

    valid_status_codes = Column(NestedMutableJson, nullable=True)
    require_body_match = Column(NestedMutableJson, nullable=True)
    require_body_not_match = Column(NestedMutableJson, nullable=True)

    scrape = relationship(
        "Scrape", back_populates="blackbox_http_config", uselist=False
    )


class OpenstackDiscovery(database.Model):
    __tablename__ = "scrape_discovery_openstack"
    id = Column(Integer, primary_key=True)
    scrape_id = Column(
        Integer, ForeignKey("scrapes.id", ondelete="CASCADE"), unique=True
    )
    port = Column(Integer, nullable=False)
    name_regex = Column(String(1023), nullable=True)

    scrape = relationship("Scrape", back_populates="openstack_discovery", uselist=False)


class StaticDiscovery(database.Model):
    __tablename__ = "scrape_discovery_static"
    id = Column(Integer, primary_key=True)
    scrape_id = Column(
        Integer, ForeignKey("scrapes.id", ondelete="CASCADE"), unique=False
    )

    host = Column(String(1023), nullable=False)
    port = Column(Integer, nullable=False)

    scrape = relationship("Scrape", back_populates="static_discovery", uselist=False)
