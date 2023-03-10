"""Added account table

Revision ID: 24fc7be6a4f7
Revises: 6a1178d9ebfb
Create Date: 2023-02-14 00:01:31.803431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24fc7be6a4f7'
down_revision = '6a1178d9ebfb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('role_name', sa.String(), nullable=True))
    op.drop_column('roles', 'rolename')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('rolename', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('roles', 'role_name')
    # ### end Alembic commands ###
