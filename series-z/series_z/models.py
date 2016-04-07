#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

#---------
#Relations
#---------

founders = Table('founders',
    Base.metadata,
    Column('founder_id', Integer, ForeignKey('founder.id')),
    Column('city_id', Integer, ForeignKey('city.id')),
    Column('company_id', Integer, ForeignKey('startup.id'))
)

cities = Table('cities',
    Base.metadata,
    Column('city_id', Integer, ForeignKey('city.id')),
    Column('person_id', Integer, ForeignKey('founder.id')),
    Column('company_id', Integer, ForeignKey('startup.id'))
)

companies = Table('companies',
    Base.metadata,
    Column('company_id', Integer, ForeignKey('company.id')),
    Column('city_id', Integer, ForeignKey('city.id')),
    Column('company_id', Integer, ForeignKey('startup.id'))
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

    __tablename__ = 'founder'

    #Founder attributes
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    angel_id = Column(String, nullable=False)
    popularity = Column(Integer)
    image_url = Column(String)
    bio = Column(String)

    #Founder foreign keys
    # location_id = Column(Integer, ForeignKey('locations.id'))

    #Founder relationships
    # location = relationship("City", back_populates="people")
    # companies = relationship("Startup", back_populates="people")

    def __init__(self, name, angel_id, popularity, image_url, bio):
        """
        Standard constructor for Founder
        """
        self.name = name
        self.angel_id = angel_id
        self.popularity = popularity
        self.image_url = image_url
        self.bio = bio

#-------
#Startup
#-------

class Startup(Base):
    """
    Startup is a class representing a startup
    """

    __tablename__ = 'startup'

    #Startup attributes
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    popularity = Column(String, nullable=False)
    market = Column(String, nullable=False)
    product_desc = Column(String)
    company_url = Column(String)
    logo_url = Column(String)

    #Startup foreign keys
    # location_id = Column(Integer, ForeignKey('locations.id'))

    #Startup relationships
    # location = relationship("City", back_populates="companies")
    # people = relationship("People", back_populates="companies")

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

    __tablename__ = 'city'

    #City attributes
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    investor_followers = Column(Integer, nullable=False)
    followers = Column(Integer, nullable=False)
    num_companies = Column(Integer, nullable=False)
    num_people = Column(Integer, nullable=False)

    #City relationships
    companies = relationship("Startup", back_populates="location")
    people = relationship("Founder", back_populates="location")

    def __init__(self, name, investor_followers, followers, num_companies, num_people):
        """
        Standard constructor for City
        """
        self.name = name
        self.investor_followers = investor_followers
        self.followers = followers
        self.num_companies = num_companies
        self.num_people = num_people


