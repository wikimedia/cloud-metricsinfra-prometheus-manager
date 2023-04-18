"""create scrape_discovery_static table

Revision ID: 8d332a4bfe2f
Revises: e5712abd9572
Create Date: 2021-10-23 16:08:40.853620

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "8d332a4bfe2f"
down_revision = "e5712abd9572"
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "scrape_discovery_static",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("scrape_id", sa.Integer(), nullable=True),
        sa.Column("host", sa.String(length=1023), nullable=False),
        sa.Column("port", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["scrape_id"], ["scrapes.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("scrape_discovery_static")
    # ### end Alembic commands ###
