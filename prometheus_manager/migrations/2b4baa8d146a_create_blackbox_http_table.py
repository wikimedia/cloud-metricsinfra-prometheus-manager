"""create blackbox http table

Revision ID: 2b4baa8d146a
Revises: b69fcb1d4f08
Create Date: 2023-09-09 14:19:20.983265

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "2b4baa8d146a"
down_revision = "b69fcb1d4f08"
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "scrape_blackbox_http",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("scrape_id", sa.Integer(), nullable=True),
        sa.Column("method", sa.String(length=255), nullable=False),
        sa.Column("headers", sa.JSON(), nullable=True),
        sa.Column("follow_redirects", sa.Boolean(), nullable=False),
        sa.Column("valid_status_codes", sa.JSON(), nullable=True),
        sa.Column("require_body_match", sa.JSON(), nullable=True),
        sa.Column("require_body_not_match", sa.JSON(), nullable=True),
        sa.ForeignKeyConstraint(["scrape_id"], ["scrapes.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("scrape_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("scrape_blackbox_http")
    # ### end Alembic commands ###
