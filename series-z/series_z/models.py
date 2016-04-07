#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
# from db import Base

# from series_z import app
# comment


Base = declarative_base()

#---------
#Relations
#---------

startup_to_founder = Table("startup_to_founder", Base.metadata,
    Column("startup_id", Integer, ForeignKey("startups.id"), primary_key=True),
    Column("founder_id", Integer, ForeignKey("founders.id"), primary_key=True)
)

#------
#Founder
#------
"""
{'angel_id': 80212,
  'bio': u'Founder & CEO of @calm  - working to bring the amazing benefits of meditation to a busy world',
  'image_url': u'https://d1qb2nb5cznatu.cloudfront.net/users/80212-medium_jpg?1405484501',
  'name': u'Alex Tew',
  'popularity': 1028
}
"""

class Founder(Base):
    """
    Founder is a class representing an investor or a company founder
    """

    __tablename__ = 'founders'

    #Founder attributes
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    angel_id = Column(String, nullable=False)
    popularity = Column(Integer)
    image_url = Column(String)
    bio = Column(String)
    rank = Column(Integer)
    num_startups = Column(Integer)
    city_name = Column(String)
    #Founder foreign keys
    city_id = Column(Integer, ForeignKey('cities.id'))

    #Founder relationships
    city = relationship("City", back_populates="founders")
    startups = relationship("Startup", secondary=startup_to_founder, back_populates="founders")

    def __init__(self, name, angel_id, popularity, image_url, bio):
        """
        Standard constructor for Founder
        """
        self.name = name
        self.angel_id = angel_id
        self.popularity = popularity
        self.image_url = image_url
        self.bio = bio
        self.rank = rank
        self.num_startups = num_startup
        self.city_name = city_nam

#-------
#Startup
#-------

class Startup(Base):
    """
    Startup is a class representing a startup
    """

    __tablename__ = 'startups'

    #Startup attributes
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    popularity = Column(String, nullable=False)
    market = Column(String, nullable=False)
    num_founders = Column(String, nullable=False)
    product_desc = Column(String)
    company_url = Column(String)
    logo_url = Column(String)

    #Startup foreign keys
    city_id = Column(Integer, ForeignKey('cities.id'))

    #Startup relationships
    city = relationship("City", back_populates="startups")
    founders = relationship("Founder", secondary=startup_to_founder, back_populates="startups")

    def __init__(self, name, location, popularity, market, product_desc, company_url, logo_url):
        """
        Standard constructor for Startup
        """
        self.name = name
        self.location = location
        self.popularity = popularity
        self.market = market
        self.product_desc = product_desc
        self.company_url = company_url
        self.logo_url = logo_url

#--------
#City
#--------

class City(Base):
    """
    City is a class representing a geographical region that hosts People and Companies
    """

    __tablename__ = 'cities'

    #City attributes
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    investor_followers = Column(Integer, nullable=False)
    popularity = Column(Integer, nullable=False)
    num_companies = Column(Integer, nullable=False)
    num_people = Column(Integer, nullable=False)

    #City relationships
    startups = relationship("Startup", back_populates="cities")
    founders = relationship("Founder", back_populates="cities")

    def __init__(self, name, investor_followers, popularity, num_companies, num_people):
        """
        Standard constructor for City
        """
        self.name = name
        self.investor_followers = investor_followers
        self.popularity = popularity
        self.num_companies = num_companies
        self.num_people = num_people


# # models for which we want to create API endpoints
# app.config['API_MODELS'] = {'companies': Startup,
#                             'people': Founder,
#                             'cities': City}

# # models for which we want to create CRUD-style URL endpoints,
# # and pass the routing onto our AngularJS application
# app.config['CRUD_URL_MODELS'] = {'companies': Startup,
#                                  'people': Founder,
#                                  'cities': City}
