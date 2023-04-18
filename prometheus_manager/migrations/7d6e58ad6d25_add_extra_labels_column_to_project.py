"""add extra_labels column to project

Revision ID: 7d6e58ad6d25
Revises: 45f4e82ee5bb
Create Date: 2023-04-18 12:24:34.267404

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "7d6e58ad6d25"
down_revision = "45f4e82ee5bb"
branch_labels = ()
depends_on: None = None


def upgrade():
    op.add_column(
        "projects",
        sa.Column("extra_labels", sa.JSON(), nullable=False, server_default="{}"),
    )


def downgrade():
    op.drop_column("projects", "extra_labels")
