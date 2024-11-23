"""Add column for member photo

Revision ID: 864d4e7707ab
Revises: 0422a147fab6
Create Date: 2024-11-23 03:06:26.304399

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '864d4e7707ab'
down_revision: Union[str, None] = '0422a147fab6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('members', sa.Column('photo_url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('members', 'photo_url')
    # ### end Alembic commands ###