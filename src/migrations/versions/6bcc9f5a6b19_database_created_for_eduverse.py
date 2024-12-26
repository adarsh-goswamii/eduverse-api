"""Database created for eduverse

Revision ID: 6bcc9f5a6b19
Revises: 13d2767d22af
Create Date: 2024-12-26 11:40:19.406723

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6bcc9f5a6b19'
down_revision: Union[str, None] = '13d2767d22af'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('access',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('api_endpoint_regex', sa.String(length=5000), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='eduverse'
    )
    op.create_index(op.f('ix_eduverse_access_id'), 'access', ['id'], unique=False, schema='eduverse')
    op.create_table('role',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='eduverse'
    )
    op.create_index(op.f('ix_eduverse_role_id'), 'role', ['id'], unique=False, schema='eduverse')
    op.create_table('tag',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='eduverse'
    )
    op.create_index(op.f('ix_eduverse_tag_id'), 'tag', ['id'], unique=False, schema='eduverse')
    op.create_table('role_access_association',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('access_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['access_id'], ['eduverse.access.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['eduverse.role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='eduverse'
    )
    op.create_index(op.f('ix_eduverse_role_access_association_id'), 'role_access_association', ['id'], unique=False, schema='eduverse')
    op.create_table('user',
    sa.Column('id', sa.BIGINT(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('fullname', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.String(length=100), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['eduverse.role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='eduverse'
    )
    op.create_table('playlist',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=5000), nullable=True),
    sa.Column('thumbnail_url', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['eduverse.user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='eduverse'
    )
    op.create_index(op.f('ix_eduverse_playlist_id'), 'playlist', ['id'], unique=False, schema='eduverse')
    op.create_index(op.f('ix_eduverse_playlist_title'), 'playlist', ['title'], unique=False, schema='eduverse')
    op.create_table('playlist_tag_association',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.Column('playlist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['playlist_id'], ['eduverse.playlist.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['eduverse.tag.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='eduverse'
    )
    op.create_index(op.f('ix_eduverse_playlist_tag_association_id'), 'playlist_tag_association', ['id'], unique=False, schema='eduverse')
    op.create_table('video',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=5000), nullable=True),
    sa.Column('thumbnail_url', sa.String(length=255), nullable=True),
    sa.Column('raw_video_url', sa.String(length=255), nullable=True),
    sa.Column('transcoding_status', sa.Enum('PENDING', 'PROCESSING', 'FAILED', 'COMPLETED', name='videotranscodingstatus'), nullable=True),
    sa.Column('uploaded_at', sa.DateTime(), nullable=True),
    sa.Column('transcoded_video_url', sa.String(length=255), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('like_count', sa.Integer(), nullable=True),
    sa.Column('playlist_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['playlist_id'], ['eduverse.playlist.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['eduverse.user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='eduverse'
    )
    op.create_index(op.f('ix_eduverse_video_id'), 'video', ['id'], unique=False, schema='eduverse')
    op.create_index(op.f('ix_eduverse_video_title'), 'video', ['title'], unique=False, schema='eduverse')
    op.create_table('user_video_history',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('watched_at', sa.DateTime(), nullable=True),
    sa.Column('max_timestamp', sa.Integer(), nullable=True),
    sa.Column('video_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['eduverse.user.id'], ),
    sa.ForeignKeyConstraint(['video_id'], ['eduverse.video.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='eduverse'
    )
    op.create_index(op.f('ix_eduverse_user_video_history_id'), 'user_video_history', ['id'], unique=False, schema='eduverse')
    op.create_table('video_like',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('liked_at', sa.DateTime(), nullable=True),
    sa.Column('video_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['eduverse.user.id'], ),
    sa.ForeignKeyConstraint(['video_id'], ['eduverse.video.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='eduverse'
    )
    op.create_index(op.f('ix_eduverse_video_like_id'), 'video_like', ['id'], unique=False, schema='eduverse')
    op.create_table('video_tag_association',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('liked_at', sa.DateTime(), nullable=True),
    sa.Column('video_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['eduverse.user.id'], ),
    sa.ForeignKeyConstraint(['video_id'], ['eduverse.video.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='eduverse'
    )
    op.create_index(op.f('ix_eduverse_video_tag_association_id'), 'video_tag_association', ['id'], unique=False, schema='eduverse')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_eduverse_video_tag_association_id'), table_name='video_tag_association', schema='eduverse')
    op.drop_table('video_tag_association', schema='eduverse')
    op.drop_index(op.f('ix_eduverse_video_like_id'), table_name='video_like', schema='eduverse')
    op.drop_table('video_like', schema='eduverse')
    op.drop_index(op.f('ix_eduverse_user_video_history_id'), table_name='user_video_history', schema='eduverse')
    op.drop_table('user_video_history', schema='eduverse')
    op.drop_index(op.f('ix_eduverse_video_title'), table_name='video', schema='eduverse')
    op.drop_index(op.f('ix_eduverse_video_id'), table_name='video', schema='eduverse')
    op.drop_table('video', schema='eduverse')
    op.drop_index(op.f('ix_eduverse_playlist_tag_association_id'), table_name='playlist_tag_association', schema='eduverse')
    op.drop_table('playlist_tag_association', schema='eduverse')
    op.drop_index(op.f('ix_eduverse_playlist_title'), table_name='playlist', schema='eduverse')
    op.drop_index(op.f('ix_eduverse_playlist_id'), table_name='playlist', schema='eduverse')
    op.drop_table('playlist', schema='eduverse')
    op.drop_table('user', schema='eduverse')
    op.drop_index(op.f('ix_eduverse_role_access_association_id'), table_name='role_access_association', schema='eduverse')
    op.drop_table('role_access_association', schema='eduverse')
    op.drop_index(op.f('ix_eduverse_tag_id'), table_name='tag', schema='eduverse')
    op.drop_table('tag', schema='eduverse')
    op.drop_index(op.f('ix_eduverse_role_id'), table_name='role', schema='eduverse')
    op.drop_table('role', schema='eduverse')
    op.drop_index(op.f('ix_eduverse_access_id'), table_name='access', schema='eduverse')
    op.drop_table('access', schema='eduverse')
    # ### end Alembic commands ###
