#!/usr/bin/python3
"""user model"""

from sqlalchemy import Column, String
from models.basemodel import BaseModel, Base
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """A class for user model"""
    __tablename__ = 'user'
    email = Column(String(45), nullable=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    username = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    stories = relationship("Story", backref="user", cascade="all, delete, delete-orphan")
