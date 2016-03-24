#!/usr/bin/env python3

from sqlalchemy import *

Base = declarative_base()

class Politician(Base):
    __tablename__ = 'politicians'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    party = Column(String)

    region_id = Column(Integer, ForeignKey('regions.id'))

    region = relationship("Region", back_populates="regions")
    donations = relationship("Donation", back_populates="donations")

class Donator(Base):
    __tablename__ = 'donators'
    
    id = Column(Integer, primary_key=True)

    donations = relationship("Donation", back_populates="donations")

class Region(Base):
    __tablename__ = 'regions'
    
    id = Column(Integer, primary_key=True)

    politicians = relationship("Politician", back_populates="politicians")

class Donation(Base):
    __tablename__ = 'donations'
    
    id = Column(Integer, primary_key=True)
    politician_id = Column(Integer, ForeignKey('politicians.id'))
    donator_id = Column(Integer, ForeignKey('donators.id'))

    politician = relationship("Politician", back_populates="politicians")
    donator = relationship("Donator", back_populates="donators")
