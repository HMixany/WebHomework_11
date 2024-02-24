"""Delete column birthday_this_year

Revision ID: 325eb7f77f41
Revises: 97c74843fd7b
Create Date: 2024-02-24 23:09:09.051897

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '325eb7f77f41'
down_revision: Union[str, None] = '97c74843fd7b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
