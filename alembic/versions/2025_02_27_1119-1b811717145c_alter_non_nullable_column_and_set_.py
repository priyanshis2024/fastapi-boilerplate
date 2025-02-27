"""Alter non nullable column and set default values

Revision ID: 1b811717145c
Revises: e8bcbe6fb338
Create Date: 2025-02-27 11:19:06.789065

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import func

# revision identifiers, used by Alembic.
revision: str = '1b811717145c'
down_revision: Union[str, None] = 'e8bcbe6fb338'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Set default values for existing columns
    op.alter_column('user', 'first_name', existing_type=sa.String(512), nullable=False, server_default="demo")
    op.alter_column('user', 'last_name', existing_type=sa.String(512), nullable=False, server_default="user")
    op.alter_column('user', 'gender', existing_type=sa.INTEGER(), nullable=False, server_default="2")

def downgrade():
    # Remove default values in case of rollback
    op.alter_column('user', 'first_name', existing_type=sa.String(512), nullable=False, server_default=None)
    op.alter_column('user', 'last_name', existing_type=sa.String(512), nullable=False, server_default=None)
    op.alter_column('user', 'gender', existing_type=sa.INTEGER(), nullable=False, server_default=None)
