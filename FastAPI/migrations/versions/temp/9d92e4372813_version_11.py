"""version 11

Revision ID: 9d92e4372813
Revises: 29b267ef41a0
Create Date: 2021-02-08 09:19:33.417952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d92e4372813'
down_revision = '29b267ef41a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('diecuts', sa.Column('col_test', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('diecuts', 'col_test')
    # ### end Alembic commands ###
