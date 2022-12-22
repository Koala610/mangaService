"""added new colums

Revision ID: 75a4fddb6e4a
Revises: 4fe2af9d81de
Create Date: 2022-12-22 21:53:42.721797

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '75a4fddb6e4a'
down_revision = '4fe2af9d81de'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bookmarks_per_page', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('technical_info', sa.LargeBinary(), nullable=True))
    op.add_column('users', sa.Column('is_subscribed', sa.Boolean(), nullable=True))
    op.drop_column('users', 'id')
    op.drop_column('users', 'tg_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('tg_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('id', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('users', 'is_subscribed')
    op.drop_column('users', 'technical_info')
    op.drop_column('users', 'bookmarks_per_page')
    # ### end Alembic commands ###