"""init

Revision ID: dd835b6ff748
Revises: 
Create Date: 2022-12-24 09:04:59.644439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd835b6ff748'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('bookmarks_hash', sa.BigInteger(), nullable=True),
    sa.Column('bookmarks_per_page', sa.Integer(), nullable=True),
    sa.Column('technical_info', sa.LargeBinary(), nullable=True),
    sa.Column('is_subscribed', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
