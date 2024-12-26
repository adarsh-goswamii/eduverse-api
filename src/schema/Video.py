from src.configs.db_constants import DBTables, DBConfig
from sqlalchemy import Column, String, Enum, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import (
  BIGINT
)
from src.configs.enums import VideoTranscodingStatus
from datetime import datetime
from src.schema.main import Base

class Video(Base):
  __tablename__ = DBTables.VIDEO
  __table_args__ = {'schema': DBConfig.SCHEMA_NAME}
  
  # Indexed columns
  id = Column(BIGINT, primary_key=True, autoincrement=True, index=True)
  title = Column(String(255), nullable=False, index=True)
  
  description = Column(String(5000))
  thumbnail_url = Column(String(255))
  raw_video_url = Column(String(255))
  transcoding_status = Column(Enum(VideoTranscodingStatus), default=VideoTranscodingStatus.PENDING)
  uploaded_at = Column(DateTime, default=datetime.utcnow)
  transcoded_video_url = Column(String(255))
  duration = Column(Integer)
  like_count = Column(Integer)
  
  # Foreign keys  
  playlist_id = Column(Integer, ForeignKey(f'{DBConfig.SCHEMA_NAME}.{DBTables.PLAYLIST}.id'))
  user_id = Column(Integer, ForeignKey(f'{DBConfig.SCHEMA_NAME}.{DBTables.USER}.id'), nullable=False)
  

  