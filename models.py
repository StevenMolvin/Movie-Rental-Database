#!/usr/bin/env python3

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

if __name__ == '__main__':
    # Create the database engine
    engine = create_engine('sqlite:///movie_rental.db')
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()
    
# Define the Movie class
class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    length = Column(String)
    release_date = Column(DateTime)
    
# Define the Customer class
class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
# Define the Rental class
class Rental(Base):
    __tablename__ = 'rentals'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    movie_id = Column(Integer, ForeignKey('movies.id'))
    rental_date = Column(DateTime, default=datetime.now)
    return_date = Column(DateTime)
    
    
    
    