#!/usr/bin/python3
"""Basemodel for rest of the models"""

from datetime import datetime
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class BaseModel:
    """Base model class """
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(String(60), default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialize a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)


    def to_dict(self):
        """return a dictionary all instances of the class"""
        dict = {}
        dict.update(self.__dict__)
        if '_sa_instance_state' in dict:
            del dict['_sa_instance_state']
        dict['created_at'] = self.created_at.isoformat()
        return dict
        
