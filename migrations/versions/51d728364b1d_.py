"""empty message

Revision ID: 51d728364b1d
Revises: 9a06ec33adea
Create Date: 2020-10-14 06:16:41.533188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51d728364b1d'
down_revision = '9a06ec33adea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_alert_lost_point', table_name='alert')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('idx_alert_lost_point', 'alert', ['lost_point'], unique=False)
    # ### end Alembic commands ###
