from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, MetaData, Text
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///library.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

metadata = MetaData()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    user_name = Column(String())
    email = Column(String(), unique=True)
    first_name = Column(String())
    last_name = Column(String())
    phone_number = Column(Integer())
    address = Column(String())

   
    
    students = relationship('Student', back_populates='user')
    borrowed_books = relationship('BookBorrower', back_populates='user')
    
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    address = Column(String())
    school_name = Column(String())
    user_id = Column(Integer(), ForeignKey("users.id"))
    
    
    user = relationship('User', back_populates='students')

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    author = Column(String())
    shelf_number = Column(String())
    description = Column(String())

    
    borrowers = relationship('BookBorrower', back_populates='books')

    
class BookBorrower(Base):
    __tablename__ = "book_borrowers"

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey("users.id"))
    book_id = Column(Integer(), ForeignKey("books.id"))
    borrowed_date = Column(String())  
    borrowed_time = Column(String())
    return_date = Column(String())
    return_time = Column(String())
    borrower_address = Column(String())   
    
    
    user = relationship('User', back_populates='borrowed_books')
    books = relationship('Book', back_populates='borrowers')
