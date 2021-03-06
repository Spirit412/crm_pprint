"""version 21

Revision ID: 1c55725c4b88
Revises: 8a37e0045c25
Create Date: 2021-03-05 08:06:49.041168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c55725c4b88'
down_revision = '8a37e0045c25'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('role', sa.String(length=100), nullable=False))
    op.drop_constraint('roles_name_key', 'roles', type_='unique')
    op.create_unique_constraint(None, 'roles', ['role'])
    op.drop_column('roles', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'roles', type_='unique')
    op.create_unique_constraint('roles_name_key', 'roles', ['name'])
    op.drop_column('roles', 'role')
    # ### end Alembic commands ###
