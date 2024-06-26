"""create scrapes tables

Revision ID: c0cce8b836fe
Revises: d17f242b71a8
Create Date: 2021-07-19 11:28:11.400383

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "c0cce8b836fe"
down_revision = "d17f242b71a8"
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "scrapes",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("project_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.ForeignKeyConstraint(["project_id"], ["projects.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("project_id", "name", name="u_project_name"),
    )
    op.create_table(
        "scrape_discovery_openstack",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("scrape_id", sa.Integer(), nullable=True),
        sa.Column("port", sa.Integer(), nullable=False),
        sa.Column("name_regex", sa.String(length=1023), nullable=True),
        sa.ForeignKeyConstraint(["scrape_id"], ["scrapes.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("scrape_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("scrape_discovery_openstack")
    op.drop_table("scrapes")
    # ### end Alembic commands ###
