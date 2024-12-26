from src.configs.db_constants import DBTables, DBConfig
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import (
  BIGINT
)
from datetime import datetime
from src.schema.main import Base

class Playlist(Base):
  __tablename__ = DBTables.PLAYLIST
  __table_args__ = {'schema': DBConfig.SCHEMA_NAME}
  
  # Indexed columns
  id = Column(BIGINT, primary_key=True, autoincrement=True, index=True)
  title = Column(String(255), nullable=False, index=True)
  
  description = Column(String(5000))
  thumbnail_url = Column(String(255))
  created_at = Column(DateTime, default=datetime.utcnow)
  
  # Foreign keys
  user_id = Column(Integer, ForeignKey(f'{DBConfig.SCHEMA_NAME}.{DBTables.USER}.id'), nullable=False)