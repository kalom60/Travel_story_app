#!/usr/bin/python3
"""Story model"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from models.basemodel import BaseModel, Base

class Story(BaseModel, Base):
    """A class for story model"""
    __tablename__ = 'story'
    title = Column(String(30), nullable=False)
    Country = Column(String(20), nullable=False)
    City = Column(String(20))
    story = Column(LONGTEXT, nullable=False)
    user_id = Column(String(60), ForeignKey('user.id'), nullable=False)

