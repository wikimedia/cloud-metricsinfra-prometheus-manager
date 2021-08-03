'''query to expr

Revision ID: ea4c92eef10c
Revises: 1a404a44c724
Create Date: 2021-08-03 10:48:04.532894

'''
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'ea4c92eef10c'
down_revision = '1a404a44c724'
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('alerts') as bop:
        bop.alter_column(
            'query', type_=sa.String(length=2048), nullable=True, new_column_name='expr'
        )
    with op.batch_alter_table('global_alerts') as bop:
        bop.alter_column(
            'query', type_=sa.String(length=2048), nullable=True, new_column_name='expr'
        )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('alerts') as bop:
        bop.alter_column(
            'expr', type_=sa.String(length=2048), nullable=True, new_column_name='query'
        )
    with op.batch_alter_table('global_alerts') as bop:
        bop.alter_column(
            'expr', type_=sa.String(length=2048), nullable=True, new_column_name='query'
        )
    # ### end Alembic commands ###