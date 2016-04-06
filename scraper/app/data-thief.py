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
	pass

def populateBylocation(locationID):

	query = session.query(Current).filter(Current.location_id == locationID).order_by('timestamp desc').limit(1)

	if len(current) > 0:
		current = query[0]
		page_num = current['page_num']
		startup_count = current['page_num'] * current['per_page']
		data = al.get_tags_startups(locationID, page_num)
		startups = data['startups']
	else:
		data = al.get_tags_startups(locationID, 1)
		current['total'] = data['total']
		current['per_page'] = data['per_page']
		current['page_num'] = data['page']
		current['last_page'] = data['last_page']
		current['location_id'] = locationID
		startups = data['startups']
		startup_count = 0

	for startup in startups:
		if not startup['hidden']:
			startup_id = startup['id']
			startup_info = buildStartupInfo(startup)
			startup_obj = Company(**startup_info)
			populateStartup(startup_obj)

			location_id = startup['location'][0]['id']
			location_name = startup_info['location']
			location_info = buildlocationInfo(location_id)
			location_obj = Location(**location_info)


def buildStartupInfo(startup):

	startup_info = {
		'name'  		 : startup['name']
		'location'  	 : startup['locations'][0]['display_name']
		'follower_count' : startup['follower_count']
		'num_investors'  : 0
		'market'  		 : startup['markets'][0]['display_name']
		'product_desc'   : startup['product_desc']
		'company_url'  	 : startup['company_url']
		'logo_url'  	 : startup['logo_url']
		'company_type'   : startup['company_type'][0]['display_name']
	}

	return startup_info

def buildLocationInfo(location_id):

	location = al.get_tags(location_id)

	location_info = {
	    'name' : location['display_name']
	    'investor_followers' : location['statistics']['investor_followers']
	    'followers' : location['statistics']['followers']
	    'num_companies' : 0
	    'num_people' : 0
	}

	return location_info

def getPersonInfo(personID):
	pass

def populateStartup(startup_obj):
	try:
		session.add(startup_obj)
		session.commit(startup_obj)
	except:
		logger.info(datetime.now() + "| Failed to commit startup object.")

def populateLocation(location_obj):


def populatePerson():
	pass

def locationExists(location_name):

	if Session.query(exists().where(Location.name == location_name))

