#!/usr/bin/env python3

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from db import Base


class Guest(Base):
    __tablename__ = 'guests'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)

    def __repr__(self):
        return "[Guest: id={}, name={}]".format(self.id, self.name)

#------
#Person
#------

class Person(Base):
    """
    Person is a class representing an investor or a company founder
    """

    __tablename__ = 'people'

    #Person attributes
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    founder = Column(Boolean, nullable=False)
    investor = Column(Boolean, nullable=False)
    num_companies = Column(Integer, nullable=False)
    image = Column(String)
    bio = Column(String)

    #Person foreign keys
    location_id = Column(Integer, ForeignKey('locations.id'))

    #Person relationships
    connections = relationship("Connection", back_populates="connections")
    location = relationship("Location", back_populates="locations")

    def __init__(self, name, location, founder, investor, num_companies):
        """
        Standard constructor for Person
        """
        self.name = name
        self.location = location
        self.founder = founder
        self.investor = investor
        self.num_companies = num_companies

#-------
#Company
#-------

class Company(Base):
    """
    Company is a class representing a startup or VC Firm
    """

    __tablename__ = 'companies'

    #Company attributes
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    follower_count = Column(String, nullable=False)
    num_investors = Column(Integer, nullable=False)
    market = Column(String, nullable=False)
    product_desc = Column(String)
    company_url = Column(String)
    logo_url = Column(String)

    #Company foreign keys
    person_id = Column(Integer, ForeignKey('locations.id'))

    #Company relationships
    connections = relationship("Connection", back_populates="connections")
    location = relationship("Location", back_populates="locations")

    def __init__(self, name, location, follower_count, num_investors, market):
        """
        Standard constructor for Company
        """
        self.name = name
        self.location = location
        self.follower_count = follower_count
        self.num_investor = num_investors
        self.market = market

#--------
#Location
#--------

class Location(Base):
    """
    Location is a class representing a geographical region that hosts People and Companies
    """

    __tablename__ = 'locations'

    #Location attributes
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    investor_followers = Column(Integer, nullable=False)
    followers = Column(Integer, nullable=False)
    num_companies = Column(Integer, nullable=False)
    num_people = Column(Integer, nullable=False)

    #Location relationships
    companies = relationship("Company", back_populates="companies")
    people = relationship("Person", back_populates="people")

    def __init__(self, name, investor_followers, followers, num_companies, num_people):
        """
        Standard constructor for Location
        """
        self.name = name
        self.investor_followers = investor_followers
        self.followers = followers
        self.num_companies = num_companies
        self.num_people = num_people

class Connection(Base):
    """
    Connection is a class that facilitates the many to many relationship between people and companies
    """

    __tablename__ = 'connections'

    id = Column(Integer, primary_key=True)

    #Connection foreign keys
    person_id = Column(Integer, ForeignKey('people.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))

    #Connection relationships
    person = relationship("Person", back_populates="people")
    company = relationship("Company", back_populates="companies")
