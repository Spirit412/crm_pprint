"""version 01

Revision ID: b3da5df9acdb
Revises: c89afba0741a
Create Date: 2021-03-29 15:44:23.431539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3da5df9acdb'
down_revision = 'c89afba0741a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('digital_jobs_print', sa.Column('diecut_cut_name', sa.String(length=60), nullable=False))
    op.alter_column('digital_jobs_print', 'customer_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_foreign_key(None, 'digital_jobs_print', 'diecuts', ['diecut_cut_name'], ['cut_name'])
    op.add_column('rows_frame', sa.Column('design_angle_rotate', sa.Integer(), nullable=False))
    op.add_column('rows_frame', sa.Column('design_url', sa.String(), nullable=False))
    op.add_column('rows_frame', sa.Column('row_number', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rows_frame', 'row_number')
    op.drop_column('rows_frame', 'design_url')
    op.drop_column('rows_frame', 'design_angle_rotate')
    op.drop_constraint(None, 'digital_jobs_print', type_='foreignkey')
    op.alter_column('digital_jobs_print', 'customer_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('digital_jobs_print', 'diecut_cut_name')
    # ### end Alembic commands ###
