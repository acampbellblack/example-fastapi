"""add content column to posts table

Revision ID: e9a4c385c926
Revises: e082ec51d92c
Create Date: 2022-02-18 21:30:33.650589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9a4c385c926'
down_revision = 'e082ec51d92c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')
