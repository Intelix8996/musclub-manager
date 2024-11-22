"""Initial migration

Revision ID: 85e20e7326a3
Revises: 
Create Date: 2024-11-11 00:41:15.025687

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '85e20e7326a3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('instruments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_instruments_id'), 'instruments', ['id'], unique=False)
    op.create_table('members',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=False),
    sa.Column('contacts', sa.String(), nullable=False),
    sa.Column('status', sa.Enum('active', 'inactive', 'retired', name='status_enum'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_members_id'), 'members', ['id'], unique=False)
    op.create_table('specialisations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_specialisations_id'), 'specialisations', ['id'], unique=False)
    op.create_table('member_instrument_relation',
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('instruments_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['instruments_id'], ['instruments.id'], ),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], )
    )
    op.create_table('member_specialisation_relation',
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('spec_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], ),
    sa.ForeignKeyConstraint(['spec_id'], ['specialisations.id'], )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('member_specialisation_relation')
    op.drop_table('member_instrument_relation')
    op.drop_index(op.f('ix_specialisations_id'), table_name='specialisations')
    op.drop_table('specialisations')
    op.drop_index(op.f('ix_members_id'), table_name='members')
    op.drop_table('members')
    op.drop_index(op.f('ix_instruments_id'), table_name='instruments')
    op.drop_table('instruments')
    # ### end Alembic commands ###
