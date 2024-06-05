"""fix unnecessary unique keys

Revision ID: a560c23bf970
Revises: a4ae1f9b9703
Create Date: 2023-10-30 16:28:11.280770

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = "a560c23bf970"
down_revision = "a4ae1f9b9703"
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("u_project_name", table_name="alerts")
    op.drop_index("u_name", table_name="global_alerts")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index("u_name", "global_alerts", ["name"], unique=False)
    op.create_index("u_project_name", "alerts", ["project_id", "name"], unique=False)
    # ### end Alembic commands ###
