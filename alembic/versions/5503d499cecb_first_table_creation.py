"""first table creation

Revision ID: 5503d499cecb
Revises: d9d74adce69a
Create Date: 2023-02-05 16:07:35.037363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5503d499cecb'
down_revision = 'd9d74adce69a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('attendances', sa.Column('date', sa.String(), nullable=True))
    op.add_column('roles', sa.Column('rolename', sa.String(), nullable=True))
    op.drop_column('roles', 'name')
    op.add_column('users', sa.Column('fullname', sa.String(), nullable=True))
    op.drop_column('users', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('users', 'fullname')
    op.add_column('roles', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('roles', 'rolename')
    op.drop_column('attendances', 'date')
    # ### end Alembic commands ###
