#!/usr/bin/env python3

from sqlalchemy import Integer, String, Boolean, ForeignKey
# from sqlalchemy.orm import relationship
from app import db


association_table = db.Table('person_to_company',
    db.Column('person_id', db.Integer, db.ForeignKey('people.id')),
    db.Column('company_id', db.Integer, db.ForeignKey('companies.id'))
)

class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(256), nullable=False)

    def __repr__(self):
        return "[Guest: id={}, name={}]".format(self.id, self.name)

class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)

    def __init__(self, text):
        self.text = text
        self.date_posted = datetime.datetime.now()

#------
#Person
#------

class Person(db.Model):
    """
    Person is a class representing an investor or a company founder
    """

    __tablename__ = 'people'

    #Person attributes
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String, nullable=False)
    location = db.Column(String, nullable=False)
    founder = db.Column(Boolean, nullable=False)
    investor = db.Column(Boolean, nullable=False)
    num_companies = db.Column(Integer, nullable=False)
    image = db.Column(String)
    bio = db.Column(String)

    #Person foreign keys
    location_id = db.Column(Integer, ForeignKey('locations.id'))

    #Person db.relationships
    connections = db.relationship("Connection", back_populates="connections")
    location = db.relationship("Location", back_populates="locations")

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

class Company(db.Model):
    """
    Company is a class representing a startup or VC Firm
    """

    __tablename__ = 'companies'

    #Company attributes
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String, nullable=False)
    location = db.Column(String, nullable=False)
    follower_count = db.Column(String, nullable=False)
    num_investors = db.Column(Integer, nullable=False)
    market = db.Column(String, nullable=False)
    product_desc = db.Column(String)
    company_url = db.Column(String)
    logo_url = db.Column(String)

    #Company foreign keys
    person_id = db.Column(Integer, ForeignKey('locations.id'))

    #Company db.relationships
    # connections = db.relationship("Connection", back_populates="connections")
    location = db.relationship("Location", back_populates="locations")

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

class Location(db.Model):
    """
    Location is a class representing a geographical region that hosts People and Companies
    """

    __tablename__ = 'locations'

    #Location attributes
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String, nullable=False)
    investor_followers = db.Column(Integer, nullable=False)
    followers = db.Column(Integer, nullable=False)
    num_companies = db.Column(Integer, nullable=False)
    num_people = db.Column(Integer, nullable=False)

    #Location db.relationships
    companies = db.relationship("Company", back_populates="companies")
    people = db.relationship("Person", back_populates="people")

    def __init__(self, name, investor_followers, followers, num_companies, num_people):
        """
        Standard constructor for Location
        """
        self.name = name
        self.investor_followers = investor_followers
        self.followers = followers
        self.num_companies = num_companies
        self.num_people = num_people

# class Connection(db.Model):
#     """
#     Connection is a class that facilitates the many to many db.relationship between people and companies
#     """

#     __tablename__ = 'connections'

#     id = db.Column(Integer, primary_key=True)

#     #Connection foreign keys
#     person_id = db.Column(Integer, ForeignKey('people.id'))
#     company_id = db.Column(Integer, ForeignKey('companies.id'))

#     #Connection db.relationships
#     person = db.relationship("Person", back_populates="people")
#     company = db.relationship("Company", back_populates="companies")




