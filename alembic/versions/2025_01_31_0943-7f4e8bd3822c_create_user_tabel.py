"""Create user table

Revision ID: 7f4e8bd3822c
Revises: 
Create Date: 2025-01-31 09:43:17.484194

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision: str = '7f4e8bd3822c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, nullable=False, server_default=sa.text("uuid_generate_v4()")),
        sa.Column('first_name', sa.String(), nullable=False),
        sa.Column('last_name', sa.String(), nullable=False),
        sa.Column('gender', sa.String(), nullable=False),
        sa.Column('email', sa.String(1024), nullable=True),
        sa.Column('phone_number', sa.String(20), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), onupdate=sa.text('CURRENT_TIMESTAMP')),
    )

def downgrade() -> None:
    op.drop_table('user')

