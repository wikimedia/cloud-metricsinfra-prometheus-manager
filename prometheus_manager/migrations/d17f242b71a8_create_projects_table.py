"""create projects table

Revision ID: d17f242b71a8
Create Date: 2021-07-18 20:24:45.625218

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "d17f242b71a8"
down_revision = None
branch_labels = ("default",)
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "projects",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("openstack_id", sa.String(length=255), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
        sa.UniqueConstraint("openstack_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("projects")
    # ### end Alembic commands ###
