"""update user model

Revision ID: 0612b0988605
Revises: b9ea65fa7016
Create Date: 2020-05-09 12:45:34.072582

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0612b0988605'
down_revision = 'b9ea65fa7016'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###
