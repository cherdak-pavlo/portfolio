"""002_add_event_relation

Revision ID: 002_add_event_relation
Revises: 001_create_user_table
Create Date: 2022-07-21 11:47:26.574203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002_add_event_relation'
down_revision = '001_create_user_table'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'event',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=300), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('starts_at', sa.DateTime(), nullable=False),
        sa.Column('ends_at', sa.DateTime(), nullable=False),
    )
    op.create_table(
        'user_event',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey("user.id"), nullable=False),
        sa.Column('event_id', sa.Integer(), sa.ForeignKey("event.id"), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('user_event')
    op.drop_table('event')

