from datetime import datetime
from sqlalchemy import Column, Integer, String, Date, TIMESTAMP, ForeignKey, Float, JSON, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    researcher = relationship('Researcher', uselist=False, back_populates='user')

class Researcher(Base):
    __tablename__ = 'researchers'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    # ... [keep existing fields] ...
    user = relationship('User', back_populates='researcher')