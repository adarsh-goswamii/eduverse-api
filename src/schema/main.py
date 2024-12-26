from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from src.schema.User import User
from src.schema.Video import Video
from src.schema.Access import Access
from src.schema.Playlist import Playlist
from src.schema.PlaylistTagAssociation import PlaylistTagAssociation
from src.schema.PlaylistTagAssociation import PlaylistTagAssociation
from src.schema.Role import Role
from src.schema.RoleAccessAssociation import RoleAccessAssociation
from src.schema.Tag import Tag
from src.schema.UserVideoHistory import UserVideoHistory
from src.schema.VideoLike import VideoLike
from src.schema.VideoTagAssociation import VideoTagAssociation