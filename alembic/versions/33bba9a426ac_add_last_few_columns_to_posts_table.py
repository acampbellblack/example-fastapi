"""add last few columns to posts table

Revision ID: 33bba9a426ac
Revises: 86f089f49424
Create Date: 2022-02-18 21:48:48.372807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33bba9a426ac'
down_revision = '86f089f49424'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, 
                                     server_default='true'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                     nullable=False,
                                     server_default=sa.text('now()')))


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
