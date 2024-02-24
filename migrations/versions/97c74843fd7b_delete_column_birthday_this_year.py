"""Delete column birthday_this_year

Revision ID: 97c74843fd7b
Revises: 706d2fa37186
Create Date: 2024-02-24 23:08:18.741105

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '97c74843fd7b'
down_revision: Union[str, None] = '706d2fa37186'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
