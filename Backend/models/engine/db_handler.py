#!/usr/bin/python3
""" Database handler file"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.basemodel import Base
from models.user import User
from models.story import Story

class DBHandler:
    """DB handler class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize db engine"""
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}:3306/{}'
                .format('root', 'root', 'localhost', 'story_db'),
                pool_pre_ping=True)

    def all(self, cls=None):
        """Return all objects in a class"""
        dict = {}
        for obj in self.__session.query(cls).all():
            key = type(obj).__name__ + '.' + obj.id
            dict[key] = obj
        return dict
    
    def new(self, obj):
        """add new object to database"""
        self.__session.add(obj)



    def reload(self):
        """launch the database"""
        Base.metadata.create_all(self.__engine)
        session_factor = sessionmaker(bind=self.__engine)
        Session = scoped_session(session_factor)
        self.__session = Session()

