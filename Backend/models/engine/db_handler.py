#!/usr/bin/python3
""" Database handler file"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

class DBHandler:
    """DB handler class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize db engine"""
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}:3306/{}'
                .format('root', 'root', 'localhost', 'story'),
                pool_pre_ping=True)

