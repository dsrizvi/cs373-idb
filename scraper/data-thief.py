from angel import angel
from angel.config import *
from models import *
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
logger.debug("Starting script.")


al = angel.AngelList(CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN)

engine = create_engine('sqlite:///seriesz.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

def main():


def populateByLocation(cityID):

	query = session.query(Current).order_by('timestamp desc').limit(1)

	if len(current) > 0:
		current = query[0]
		startup count = current['page_num'] * current['per_page']
	else:
		metadata = al.get_tags_startups(locationID, 1)
		current['total'] = metadata['total']
		current['per_page'] = metadata['per_page']
		current['page_num'] = metadata['page']
		current['last_page'] = metadata['last_page']
		current['city_id'] = cityID
		startup_count = 0


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