"""first migrate

Revision ID: 5803d53ef835
Revises: 
Create Date: 2023-07-23 16:57:01.521556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5803d53ef835'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('menus',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_index(op.f('ix_menus_id'), 'menus', ['id'], unique=False)
    op.create_table('submenus',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('menu_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['menu_id'], ['menus.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_index(op.f('ix_submenus_id'), 'submenus', ['id'], unique=False)
    op.create_table('dishes',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('price', sa.String(), nullable=False),
    sa.Column('submenu_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['submenu_id'], ['submenus.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_index(op.f('ix_dishes_id'), 'dishes', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_dishes_id'), table_name='dishes')
    op.drop_table('dishes')
    op.drop_index(op.f('ix_submenus_id'), table_name='submenus')
    op.drop_table('submenus')
    op.drop_index(op.f('ix_menus_id'), table_name='menus')
    op.drop_table('menus')
    # ### end Alembic commands ###
