#!/usr/bin/python3
""" Database handler file"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

class DBHandler:
    """DB handler class"""
