"""empty message

Revision ID: 13cc0537d58e
Revises: 
Create Date: 2017-11-28 13:56:16.522000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13cc0537d58e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('salt', sa.String(length=72), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'salt')
    # ### end Alembic commands ###
