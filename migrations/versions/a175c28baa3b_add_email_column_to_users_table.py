"""Add email column to users table

Revision ID: a175c28baa3b
Revises: 9be6e1fd35eb
Create Date: 2023-07-21 11:50:45.544268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a175c28baa3b'
down_revision = '9be6e1fd35eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(), nullable=False, server_default=''))

    with op.batch_alter_table('users') as batch_op:
        batch_op.create_unique_constraint('uq_users_email', ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('email')

    # ### end Alembic commands ###