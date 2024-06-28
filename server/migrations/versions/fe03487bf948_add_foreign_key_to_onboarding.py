"""add foreign key to onboarding

Revision ID: fe03487bf948
Revises: 3e1a5b355448
Create Date: 2024-06-29 01:52:24.371384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe03487bf948'
down_revision = '3e1a5b355448'
branch_labels = None
depends_on = None



def upgrade():
    # Use batch mode to alter the table
    with op.batch_alter_table('onboardings', recreate='always') as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            'fk_onboardings_employee_id_employees', 'employees', ['employee_id'], ['id']
        )


def downgrade():
    # Use batch mode to alter the table
    with op.batch_alter_table('onboardings', recreate='always') as batch_op:
        batch_op.drop_constraint('fk_onboardings_employee_id_employees', type_='foreignkey')
        batch_op.drop_column('employee_id')
