from src.configs.db_constants import DBTables, DBConfig
from sqlalchemy import Column, DateTime, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import (
  BIGINT
)
from datetime import datetime
from src.schema.main import Base

class RoleAccessAssociation(Base):
  __tablename__ = DBTables.ROLE_ACCESS_ASSOCIATION
  __table_args__ = {'schema': DBConfig.SCHEMA_NAME}
  
  # Indexed columns
  id = Column(BIGINT, primary_key=True, autoincrement=True, index=True)
  
  # Foreign keys  
  role_id = Column(Integer, ForeignKey(f'{DBConfig.SCHEMA_NAME}.{DBTables.ROLE}.id'), nullable=False)
  access_id = Column(Integer, ForeignKey(f'{DBConfig.SCHEMA_NAME}.{DBTables.ACCESS}.id'), nullable=False)
  

  