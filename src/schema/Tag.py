from src.configs.db_constants import DBTables, DBConfig
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import (
  BIGINT
)
from src.schema.main import Base

class Tag(Base):
  __tablename__ = DBTables.TAG
  __table_args__ = {'schema': DBConfig.SCHEMA_NAME}
  
  # Indexed columns
  id = Column(BIGINT, primary_key=True, autoincrement=True, index=True)
  title = Column(String(100), nullable=False)
  

  