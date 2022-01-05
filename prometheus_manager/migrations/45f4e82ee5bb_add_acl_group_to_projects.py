'''add acl_group to projects

Revision ID: 45f4e82ee5bb
Revises: 6cf9d89392b6
Create Date: 2022-01-05 15:41:13.250072

'''
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '45f4e82ee5bb'
down_revision = '6cf9d89392b6'
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('projects', sa.Column('acl_group', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('projects', 'acl_group')
    # ### end Alembic commands ###
