from src.schema.main import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from src.configs.db_constants import DBTables, DBConfig
from sqlalchemy.dialects.postgresql import (
  BIGINT
)


class User(Base):
  __tablename__ = DBTables.USER
  __table_args__ = {'schema': DBConfig.SCHEMA_NAME}
  
  id = Column(BIGINT, primary_key=True)
  email = Column(String(100), nullable=False)
  password = Column(String(100), nullable=False)
  fullname = Column(String(100), nullable=False)
  created_at = Column(String(100), nullable=False)
  
  role_id = Column(Integer, ForeignKey(f'{DBConfig.SCHEMA_NAME}.{DBTables.ROLE}.id'), nullable=False)