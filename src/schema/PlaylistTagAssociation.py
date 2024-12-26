from src.configs.db_constants import DBTables, DBConfig
from sqlalchemy import Column, DateTime, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import (
  BIGINT
)
from datetime import datetime
from src.schema.main import Base

class PlaylistTagAssociation(Base):
  __tablename__ = DBTables.PLAYLIST_TAG_ASSOCIATION
  __table_args__ = {'schema': DBConfig.SCHEMA_NAME}
  
  # Indexed columns
  id = Column(BIGINT, primary_key=True, autoincrement=True, index=True)
  
  # Foreign keys  
  tag_id = Column(Integer, ForeignKey(f'{DBConfig.SCHEMA_NAME}.{DBTables.TAG}.id'), nullable=False)
  playlist_id = Column(Integer, ForeignKey(f'{DBConfig.SCHEMA_NAME}.{DBTables.PLAYLIST}.id'), nullable=False)
  

  