"""empty message

Revision ID: 27b381148478
Revises: 6e1cbc828430
Create Date: 2020-10-21 21:14:56.543569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27b381148478'
down_revision = '6e1cbc828430'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fdog',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('comment', sa.String(length=255), nullable=True),
    sa.Column('fid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fid'], ['animal_dog.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fdog')
    # ### end Alembic commands ###