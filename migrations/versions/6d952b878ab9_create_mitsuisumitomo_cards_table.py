"""create_mitsuisumitomo_cards_table

Revision ID: 6d952b878ab9
Revises: b8787137afdf
Create Date: 2025-05-23 10:19:27.143306

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6d952b878ab9'
down_revision: Union[str, None] = 'b8787137afdf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
