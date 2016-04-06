from angel import angel
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import logging

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

def scrape():
	region_ids = []
	region_ids.append(1692)
	#region_ids.append(1664)
	num_companies = 1
	companies = get_companies(region_ids, num_companies)

    for company in companies:
        #query table for company to see if already existing
		if (session.query(Company).filter(Company.name == company['name']).count()) == 0:
        	if not company['hidden']:
            	c = enter_company(company)
				enter_connections(company)

def enter_company(company):
	location_obj = company['locations'][0]

    name = company['name']
    #ACCOUNT FOR NO LOCATION?
    location = location_obj['name']
    follower_count = company['follower_count']
    num_investors = 0
    #ACCOUNT FOR NO MARKET?
    market = company['markets'][0]['name']
    product_desc = company['product_desc']
    company_url = company['company_url']
    logo_url = company['logo_url']

    #query table for location name
    location_id = location_obj['id']
    if (session.query(Location).filter(Location.angel_id == location_id).count()) == 0:
        location_tag = al.get_tags(location_id)
        l = enter_location(location_tag)

    #upload company to Company table (make sure to include location_id)
	c = Company(name = name, location = location, follower_count = follower_count, num_investors = num_investors, market = market, product_desc = product_desc, company_url = company_url, logo_url = logo_url, location_id = location_id)

	session.add(c)
	session.commit()

	return c

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

	return l

def enter_user(user):
    name = user['name']
    #ACCOUNT FOR NO LOCATION
    location = user['locations'][0]['name']
    follower_count = user['follower_count']
    investor = False
    num_companies = 0
    image = user['image']
    bio = user['bio']

    #upload user to Person table
	u = Person(name = name, location = location, founder = founder, investor = investor, num_companies = num_companies, image = image, bio = bio)

	session.add(u)
	session.commit()

	return u

def enter_connections(company):
    founders = al.get_startup_roles(startup_id=company['id'], role=['founder'])
    #investors = al.get_startup_roles(startup_id=company['id'], role=['past_investor'])
    enter_founder_investors(founders, company)
    #enter_founder_investors(investors, company)

#not positive about the logic in this function
def enter_founder_investors(roles, company):
    role_list = roles['startup_roles']
    for role in role_list:
		user_id = role['tagged']['id']
        #query table for User name
        if (session.query(Person).filter(Person.angel_id == user_id).count()) == 0:
            user = al.get_user(user_id)
            user_obj = enter_user(user)
            company_obj = enter_company(company)

        person_id = role['tagged']['id']
        company_id = company['id']
        #upload connection into Connection table
        a = PeopleCompanyAssociation(is_founder = is_founder)
        a.person = user_obj
        company_obj.people.append(a)		

        """
        if role['tagged']['type'] == "User":
           	user_id = role['tagged']['id']
			#query table for User name
           	if (session.query(Person).filter(Person.angel_id == user_id).count()) == 0:
           		user = al.get_user(user_id)
            	user_obj = enter_user(user)
				company_obj = enter_company(company)

			if role['role'] == "founder":
				is_founder = True
			else:
				is_founder = False
            person_id = role['tagged']['id']
            company_id = company['id']
 			#upload connection into Connection table
			a = PeopleCompanyAssociation(is_founder = is_founder)
			a.person = user_obj
			company_obj.people.append(a)

		if role['tagged']['type'] == "Startup":
			#query table for Company name
            if (session.query(Company).filter(Company.angel_id == company['id']).count()) == 0:
            	investor = al.get_startup(role['tagged']['id'])
            	investor_obj = enter_company(investor)
				company_obj = enter_company(company)
            investor_id = role['tagged']['id']
            company_id = company['id']
			#upload investment into Investment table
            company_obj.companies.append(investor_obj)
        """

def get_company_ids(region_ids, num_companies):
	"""
	region_ids: a list of ids for regions from which you want company ids
	num_ids: the max number of company ids you want from each region
	"""

	companies = []

	for r_id in region_ids:
		startups = al.get_tags_startups(r_id)
		count = 0
        for startup in startups:
            if count >= num_ids:
                break
            companies.append(startup)
            count += count

	return startup_ids

