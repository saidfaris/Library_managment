from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

from sqlalchemy.ext.declarative import declarative_base

from database import session

Base = declarative_base()

