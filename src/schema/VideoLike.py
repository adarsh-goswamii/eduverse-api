from src.configs.db_constants import DBTables, DBConfig
from sqlalchemy import Column, DateTime, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import (
  BIGINT
)
from datetime import datetime
from src.schema.main import Base

class VideoLike(Base):
  __tablename__ = DBTables.VIDEO_LIKE
  __table_args__ = {'schema': DBConfig.SCHEMA_NAME}
  
  # Indexed columns
  id = Column(BIGINT, primary_key=True, autoincrement=True, index=True)
  
  liked_at = Column(DateTime, default=datetime.utcnow)
  
  # Foreign keys  
  video_id = Column(Integer, ForeignKey(f'{DBConfig.SCHEMA_NAME}.{DBTables.VIDEO}.id'), nullable=False)
  user_id = Column(Integer, ForeignKey(f'{DBConfig.SCHEMA_NAME}.{DBTables.USER}.id'), nullable=False)
  

  