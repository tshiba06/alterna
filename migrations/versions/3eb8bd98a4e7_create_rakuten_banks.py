"""create_rakuten_banks

Revision ID: 3eb8bd98a4e7
Revises: 9d8c9db7e7cc
Create Date: 2024-12-24 22:19:12.459439

"""
from datetime import datetime
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '3eb8bd98a4e7'
down_revision: Union[str, None] = '9d8c9db7e7cc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "rakuten_banks",
        sa.Column("id", type_=sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("total", type_=sa.Integer(), nullable=False),
        sa.Column(
            "created_at", type_=sa.TIMESTAMP(), nullable=False, default=datetime.now
        ),
        if_not_exists=True,
    )


def downgrade() -> None:
    op.drop_table("rakuten_banks")
