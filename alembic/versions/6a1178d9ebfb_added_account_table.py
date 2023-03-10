"""Added account table

Revision ID: 6a1178d9ebfb
Revises: 8b61e0782f10
Create Date: 2023-02-13 23:59:15.911198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a1178d9ebfb'
down_revision = '8b61e0782f10'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_roles_department', table_name='roles')
    op.drop_column('roles', 'department')
    op.drop_index('ix_users_department', table_name='users')
    op.drop_column('users', 'department')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('department', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_index('ix_users_department', 'users', ['department'], unique=False)
    op.add_column('roles', sa.Column('department', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_index('ix_roles_department', 'roles', ['department'], unique=False)
    # ### end Alembic commands ###
