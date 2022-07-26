"""created Inventory table

Revision ID: ac4ca7bc0953
Revises: 
Create Date: 2022-07-28 10:07:04.872387

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac4ca7bc0953'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inventory',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('inv_date', sa.DateTime(), nullable=True),
    sa.Column('family', sa.String(), nullable=True),
    sa.Column('facility', sa.String(), nullable=True),
    sa.Column('tank', sa.String(), nullable=True),
    sa.Column('task_id', sa.String(), nullable=True),
    sa.Column('total_animals', sa.Integer(), nullable=True),
    sa.Column('shell_lengths', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('inventory')
    # ### end Alembic commands ###
