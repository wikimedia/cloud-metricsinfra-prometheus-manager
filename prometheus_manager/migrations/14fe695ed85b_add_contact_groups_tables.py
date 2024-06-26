"""add contact groups tables

Revision ID: 14fe695ed85b
Revises: 85f1d58f533d
Create Date: 2021-08-05 14:59:05.839269

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "14fe695ed85b"
down_revision = "85f1d58f533d"
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "contact_groups",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("project_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["project_id"], ["projects.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("project_id", "name", name="u_project_name"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("contact_groups")
    # ### end Alembic commands ###
