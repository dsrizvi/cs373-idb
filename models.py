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

    connections = relationship("Connection", back_populates="connections")

class Company(Base):
    __tablename__ = 'companies'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    num_jobs = Column(Integer, nullable=False)
    num_investors = Column(Integer, nullable=False)
    tag = Column(String, nullable=False)
    product_desc = Column(String)
    company_url = Column(String)
    logo_url = Column(String)

    connections = relationship("Connection", back_populates="connections")
    jobs = relationship("Job", back_populates="jobs")

class Job(Base):
    __tablename__ = 'jobs'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    job_type = Column(String, nullable=False)
    salary_min = Column(Integer, nullable=False)
    salary_max = Column(Integer, nullable=False)
    equity_cliff = Column(Double, nullable=False)
    equity_min = Column(Double)
    equity_max = Column(Double)

    company_id = Column(Integer, ForeignKey('companies.id'))

    company = relationship("Company", back_populates="companies")

class Connection(Base):
    __tablename__ = 'connections'
    
    id = Column(Integer, primary_key=True)

    person_id = Column(Integer, ForeignKey('people.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))

    person = relationship("Person", back_populates="people")
    company = relationship("Company", back_populates="companies")
