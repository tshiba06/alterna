"""create_sumishin_sbi_banks

Revision ID: 010ca7e89990
Revises: 3eb8bd98a4e7
Create Date: 2024-12-26 16:18:37.369829

"""

from datetime import datetime
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "010ca7e89990"
down_revision: Union[str, None] = "3eb8bd98a4e7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "sumishin_sbi_banks",
        sa.Column("id", type_=sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("total", type_=sa.Integer(), nullable=False),
        sa.Column(
            "created_at", type_=sa.TIMESTAMP(), nullable=False, default=datetime.now
        ),
        if_not_exists=True,
    )


def downgrade() -> None:
    op.drop_table("sumishin_sbi_banks")
