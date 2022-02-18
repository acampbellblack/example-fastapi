"""create posts table

Revision ID: e082ec51d92c
Revises: 
Create Date: 2022-02-18 21:20:41.248393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e082ec51d92c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',
                    sa.Column('id', sa.Integer(), nullable=False,
                              primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))


def downgrade():
    op.drop_table('posts')
