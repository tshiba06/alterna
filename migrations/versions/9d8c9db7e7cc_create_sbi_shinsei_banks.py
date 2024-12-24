"""create_sbi_shinsei_banks

Revision ID: 9d8c9db7e7cc
Revises:
Create Date: 2024-12-20 21:06:24.524123

"""

from datetime import datetime
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "9d8c9db7e7cc"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "sbi_shinsei_banks",
        sa.Column("id", type_=sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("total", type_=sa.Integer(), nullable=False),
        sa.Column(
            "created_at", type_=sa.TIMESTAMP(), nullable=False, default=datetime.now
        ),
        if_not_exists=True,
    )


def downgrade() -> None:
    op.drop_table("sbi_shinsei_banks")