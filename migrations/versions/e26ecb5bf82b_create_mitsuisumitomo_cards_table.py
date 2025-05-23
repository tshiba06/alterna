"""create_mitsuisumitomo_cards_table

Revision ID: e26ecb5bf82b
Revises: 6d952b878ab9
Create Date: 2025-05-23 10:19:48.684566

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e26ecb5bf82b'
down_revision: Union[str, None] = '6d952b878ab9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
