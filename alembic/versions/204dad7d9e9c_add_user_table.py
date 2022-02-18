"""add user table

Revision ID: 204dad7d9e9c
Revises: e9a4c385c926
Create Date: 2022-02-18 21:35:19.965857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '204dad7d9e9c'
down_revision = 'e9a4c385c926'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), nullable=False, 
                              primary_key=True),
                    sa.Column('email', sa.String(), nullable=False,
                              unique=True),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
                              server_default=sa.text('now()'), nullable=False))


def downgrade():
    op.drop_table('users')
