"""version 18

Revision ID: 9ffcd85fbe9f
Revises: e5845b9caf70
Create Date: 2021-02-15 10:44:10.873101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ffcd85fbe9f'
down_revision = 'e5845b9caf70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('diecuts', sa.Column('created_on', sa.DateTime(), nullable=True))
    op.add_column('diecuts', sa.Column('updated_on', sa.DateTime(), nullable=True))
    op.add_column('zubs', sa.Column('created_on', sa.DateTime(), nullable=True))
    op.add_column('zubs', sa.Column('updated_on', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('zubs', 'updated_on')
    op.drop_column('zubs', 'created_on')
    op.drop_column('diecuts', 'updated_on')
    op.drop_column('diecuts', 'created_on')
    # ### end Alembic commands ###
