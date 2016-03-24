#!/usr/bin/env python3

from sqlalchemy import *

Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    founder = Column(Boolean, nullable=False)
    investor = Column(Boolean, nullable=False)
    num_companies = Column(Integer, nullable=False)
    image = Column(String)
    bio = Column(String)

    location_id = Column(Integer, ForeignKey('locations.id'))

    connections = relationship("Connection", back_populates="connections")
    location = relationship("Location", back_populates="locations")

    def __init__(self, name, location, founder, investor, num_companies):
        self.name = name
        self.location = location
        self.founder = founder
        self.investor = investor
        self.num_companies = num_companies

class Company(Base):
    __tablename__ = 'companies'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    follower_count = Column(String, nullable=False)
    num_investors = Column(Integer, nullable=False)
    market = Column(String, nullable=False)
    product_desc = Column(String)
    company_url = Column(String)
    logo_url = Column(String)

    person_id = Column(Integer, ForeignKey('locations.id'))

    connections = relationship("Connection", back_populates="connections")
    location = relationship("Location", back_populates="locations")
    def __init__(self, name, location, follower_count, num_investors, market):
        self.name = name
        self.location = location
        self.follower_count = follower_count
        self.num_investor = num_investors
        self.market = market

class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    investor_followers = Column(String, nullable=False)
    followers = Colunn(String, nullable=False)
    num_companies = Column(Integer, nullable=False)
    num_people = Column(Integer, nullable=False)

    companies = relationship("Company", back_populates="companies")
    people = relationship("Person", back_populates="people")

    def __init__(self, name, investor_followers, followers, num_companies, num_people):
        self.name = name
        self.investor_followers = investor_followers
        self.followers = followers
        self.num_companies = num_companies
        self.num_people = num_people

class Connection(Base):
    __tablename__ = 'connections'
    
    id = Column(Integer, primary_key=True)

    person_id = Column(Integer, ForeignKey('people.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))

    person = relationship("Person", back_populates="people")
    company = relationship("Company", back_populates="companies")
