from angel import angel
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import logging
import datetime

"""
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
logger.info(datetime.now() + "| Starting script.")

al = angel.AngelList(CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN)
logger.info(datetime.now() + "| Connected to Angel List API.")

engine = create_engine('sqlite:///seriesz.db')
logger.info(datetime.now() + "| DB engine created.")

DBSession = sessionmaker(bind=engine)
session = DBSession()
logger.info(datetime.now() + "| DB session created.")
"""

def scrape():
    location_ids = []
    location_ids.append(1692)
    #region_ids.append(1664)
    #companies = get_companies(region_ids, num_companies)

    for location_id in location_ids:
        location = al.get_tags(location_id)
        enter_location(location)
        companies = get_companies(location, 1)
        
        for company in companies:
            if (session.query(Company).filter(Company.angel_id == company['id']).count()) == 0:
                enter_company(company, location) 
                founders = al.get_startup_roles(startup_id=company['id'], role='founder')
                
                for f in founders:
                    founder = f['tagged']
                    if f['type'] == 'User' and(session.query(Person).filter(Person.angel_id == founder['id']).count()) == 0:
                        enter_user(founder, company, location)


def enter_company(company, location):
    name = company['name']
    #ACCOUNT FOR NO LOCATION?
    location_name = location['name']
    follower_count = company['follower_count']
    num_investors = 0
    #ACCOUNT FOR NO MARKET?
    market = company['markets'][0]['name']
    product_desc = company['product_desc']
    company_url = company['company_url']
    logo_url = company['logo_url']

    #upload company to Company table (make sure to include location_id)
    c = Company(name = name, location_name = location_name, follower_count = follower_count, num_investors = num_investors, market = market, product_desc = product_desc, company_url = company_url, logo_url = logo_url, location = location)

    session.add(c)
    session.commit()

def enter_location(location):
    name = location['name']
    investor_followers = location['statistics']['all']['investor_followers']
    followers = location['statistics']['all']['followers']
    num_companies = 0
    num_people = 0

    #upload location to Location table
    loc = Location(name = name, investor_followers = investor_followers, followers = followers, num_companies = num_companies, num_people = num_people)

    session.add(loc)
    session.commit()

def enter_user(founder, company, location):
    name = founder['name']
    #ACCOUNT FOR NO LOCATION
    location_name = location['name']
    follower_count = founder['follower_count']
    investor = founder['investor']
    num_companies = 0
    image = founder['image']
    bio = founder['bio']

    #upload user to Person table
    f = Person(name = name, location_name = location_name, founder = founder, investor = investor, num_companies = num_companies, image = image, bio = bio, location = location)
    f.companies.append(company)

    session.add(u)
    session.commit()


def get_company_ids(region, num_companies):
    """
    currently only works up to one page
    region: region object
    num_ids: the max number of company ids you want from each region
    """

    companies = []

    startups = al.get_tags_startups(region['id'], 1)
    count = 0
    for startup in startups:
        if count >= num_ids:
            break
        companies.append(startup)
        count += count

    return companies

