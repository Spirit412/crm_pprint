"""Second

Revision ID: 91d1ea1b3660
Revises: 94f85a7e26b8
Create Date: 2021-02-04 10:06:05.470242

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91d1ea1b3660'
down_revision = '94f85a7e26b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('diecuts',
    sa.Column('cut_name', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('cut_name')
    )
    op.create_table('zubs',
    sa.Column('zub_num', sa.Integer(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('zub_num'),
    sa.UniqueConstraint('zub_num')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('zubs')
    op.drop_table('diecuts')
    # ### end Alembic commands ###