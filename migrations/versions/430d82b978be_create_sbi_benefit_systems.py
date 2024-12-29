"""create_sbi_benefit_systems

Revision ID: 430d82b978be
Revises: 010ca7e89990
Create Date: 2024-12-29 18:23:59.765732

"""

from datetime import datetime
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "430d82b978be"
down_revision: Union[str, None] = "010ca7e89990"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "sbi_benefit_systems",
        sa.Column("id", type_=sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("total", type_=sa.Integer(), nullable=False),
        sa.Column(
            "created_at", type_=sa.TIMESTAMP(), nullable=False, default=datetime.now
        ),
        if_not_exists=True,
    )


def downgrade() -> None:
    op.drop_table("sbi_benefit_systems")
