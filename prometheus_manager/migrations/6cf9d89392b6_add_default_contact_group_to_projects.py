"""add default contact group to projects

Revision ID: 6cf9d89392b6
Revises: c3147c5d7f41
Create Date: 2021-10-23 19:20:24.939579

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "6cf9d89392b6"
down_revision = "c3147c5d7f41"
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "projects", sa.Column("default_contact_group_id", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(
        None,
        "projects",
        "contact_groups",
        ["default_contact_group_id"],
        ["id"],
        ondelete="SET NULL",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "projects", type_="foreignkey")
    op.drop_column("projects", "default_contact_group_id")
    # ### end Alembic commands ###
