"""add foreign-key to posts table

Revision ID: 86f089f49424
Revises: 204dad7d9e9c
Create Date: 2022-02-18 21:42:56.291332

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86f089f49424'
down_revision = '204dad7d9e9c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', 
                          referent_table='users', local_cols=['owner_id'], 
                          remote_cols=['id'], ondelete='CASCADE')


def downgrade():
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
