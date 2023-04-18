"""add scrape path

Revision ID: 409581df8e2d
Revises: c0cce8b836fe
Create Date: 2021-07-30 12:32:09.173506

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "409581df8e2d"
down_revision = "c0cce8b836fe"
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "scrapes",
        sa.Column(
            "path", sa.String(length=255), server_default="/metrics", nullable=False
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("scrapes", "path")
    # ### end Alembic commands ###
