"""Addedtable

Revision ID: 8b61e0782f10
Revises: a213f24be95a
Create Date: 2023-02-07 18:17:21.289193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b61e0782f10'
down_revision = 'a213f24be95a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admins', sa.Column('isActive', sa.Boolean(), nullable=True))
    op.add_column('attendances', sa.Column('attend_date', sa.DateTime(), nullable=True))
    op.drop_column('attendances', 'date')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('attendances', sa.Column('date', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('attendances', 'attend_date')
    op.drop_column('admins', 'isActive')
    # ### end Alembic commands ###
