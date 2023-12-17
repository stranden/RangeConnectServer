"""Adding base tables

Revision ID: 37dd7dbb7c38
Revises:
Create Date: 2023-12-17 16:15:57.483536

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '37dd7dbb7c38'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('CREATE SCHEMA IF NOT EXISTS rangeconnect')
    op.create_table('range_event_shooter',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('shooting_range', sa.UUID(), nullable=True),
    sa.Column('firing_point', sa.String(), nullable=False),
    sa.Column('start_number', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('club', sa.String(), nullable=True),
    sa.Column('group', sa.String(), nullable=True),
    sa.Column('created_date', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.Column('modified_date', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='rangeconnect'
    )
    op.create_index(op.f('ix_rangeconnect_range_event_shooter_id'), 'range_event_shooter', ['id'], unique=True, schema='rangeconnect')
    op.create_index(op.f('ix_rangeconnect_range_event_shooter_shooting_range'), 'range_event_shooter', ['shooting_range'], unique=False, schema='rangeconnect')
    op.create_table('range_event_shot',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('shooting_range', sa.UUID(), nullable=False),
    sa.Column('firing_point', sa.String(), nullable=False),
    sa.Column('start_number', sa.String(), nullable=False),
    sa.Column('series_type', sa.Enum('SIGHT', 'MATCH', name='seriestype'), nullable=False),
    sa.Column('shot_id', sa.Integer(), nullable=False),
    sa.Column('shot_value', sa.Float(), nullable=False),
    sa.Column('shot_value_decimal', sa.Float(), nullable=False),
    sa.Column('x_coord', sa.Float(), nullable=False),
    sa.Column('y_coord', sa.Float(), nullable=False),
    sa.Column('created_date', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.Column('modified_date', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='rangeconnect'
    )
    op.create_index(op.f('ix_rangeconnect_range_event_shot_id'), 'range_event_shot', ['id'], unique=True, schema='rangeconnect')
    op.create_index(op.f('ix_rangeconnect_range_event_shot_shooting_range'), 'range_event_shot', ['shooting_range'], unique=False, schema='rangeconnect')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_rangeconnect_range_event_shot_shooting_range'), table_name='range_event_shot', schema='rangeconnect')
    op.drop_index(op.f('ix_rangeconnect_range_event_shot_id'), table_name='range_event_shot', schema='rangeconnect')
    op.drop_table('range_event_shot', schema='rangeconnect')
    op.drop_index(op.f('ix_rangeconnect_range_event_shooter_shooting_range'), table_name='range_event_shooter', schema='rangeconnect')
    op.drop_index(op.f('ix_rangeconnect_range_event_shooter_id'), table_name='range_event_shooter', schema='rangeconnect')
    op.drop_table('range_event_shooter', schema='rangeconnect')
    op.execute('DROP SCHEMA IF EXISTS rangeconnect RESTRICT')
    # ### end Alembic commands ###