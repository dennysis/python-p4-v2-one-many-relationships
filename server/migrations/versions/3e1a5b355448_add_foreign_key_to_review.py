"""add foreign key to Review

Revision ID: 3e1a5b355448
Revises: c25c506fbb5a
Create Date: 2024-06-29 01:34:26.026875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e1a5b355448'
down_revision = 'c25c506fbb5a'
branch_labels = None
depends_on = None

def upgrade():
    # Use batch mode to alter the table
    with op.batch_alter_table('reviews', recreate='always') as batch_op:
        batch_op.create_foreign_key(
            'fk_reviews_employee_id_employees', 'employees', ['employee_id'], ['id'])

def downgrade():
    # Use batch mode to alter the table
    with op.batch_alter_table('reviews', recreate='always') as batch_op:
        batch_op.drop_constraint('fk_reviews_employee_id_employees', type_='foreignkey')