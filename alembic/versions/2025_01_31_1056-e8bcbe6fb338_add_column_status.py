"""Add column status

Revision ID: e8bcbe6fb338
Revises: 7f4e8bd3822c
Create Date: 2025-01-31 10:56:49.945037

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8bcbe6fb338'
down_revision: Union[str, None] = '7f4e8bd3822c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('user',sa.Column('status', sa.String(), nullable=False))

def downgrade() -> None:
    op.drop_column('user','status')