"""create_mitsuisumitomo_banks

Revision ID: b8787137afdf
Revises: 430d82b978be
Create Date: 2024-12-31 22:54:07.303000

"""

from datetime import datetime
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "b8787137afdf"
down_revision: Union[str, None] = "430d82b978be"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "mitsuisumitomo_banks",
        sa.Column("id", type_=sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("total", type_=sa.Integer(), nullable=False),
        sa.Column(
            "created_at", type_=sa.TIMESTAMP(), nullable=False, default=datetime.now
        ),
        if_not_exists=True,
    )


def downgrade() -> None:
    op.drop_table("mitsuisumitomo_banks")
