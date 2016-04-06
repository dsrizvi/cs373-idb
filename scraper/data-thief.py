from angel import angel
from angel.config import *
from models import *
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import logging
from datetime import datetime

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

def main():


def populateByCity(cityID):

	query = session.query(Current).filter(Current.city_id == cityID).order_by('timestamp desc').limit(1)

	if len(current) > 0:
		current = query[0]
		page_num = current['page_num']
		startup_count = current['page_num'] * current['per_page']
		data = al.get_tags_startups(cityID, page_num)
		startups = data['startups']
	else:
		data = al.get_tags_startups(locationID, 1)
		current['total'] = data['total']
		current['per_page'] = data['per_page']
		current['page_num'] = data['page']
		current['last_page'] = data['last_page']
		current['city_id'] = cityID
		startups = data['startups']
		startup_count = 0

	for startup in startups:
		name = startup['name']
		location = startup['locations'][0]['display_name']
	    follower_count = startup['']
	    num_investors = startup['']
	    market = startup['markets'][0]['display_name']
	    product_desc = startup['product_desc']
	    company_url = startup['company_url']
	    logo_url = startup['logo_url']
	    company_type = startup['company_type'][0]['display_name']


def getCompanyInfo(companyID):
	pass

def getRegionInfo(regionID):
	pass

def getPersonInfo(personID):
	pass

def populateCompany():
	pass

def populateLocation():
	pass

def populatePerson():
	pass