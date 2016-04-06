#!/usr/bin/env python3
import time, os, json, logging, sys
from angel import AngelList
from series_z.core import db
from series_z.models import *
from series_z import app

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#-----
#Setup
#-----

num_missed_startups = 0
num_missed_founders = 0
num_missed_cities = 0
num_missed_city_data = 0

def get_db_session () :
    engine = create_engine('sqlite:///series_z.db')
    logger.info("DB engine created")

    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    logger.info("DB session created")

    return session


def get_angel_list() :
    """
    Returns AngelList API object
    """
    try :
        ACCESS_TOKEN = os.environ['ANGEL_ACCESS_TOKEN']
        CLIENT_ID = os.environ['ANGEL_CLIENT_ID']
        CLIENT_SECRET = os.environ['ANGEL_CLIENT_SECRET']
    except KeyError as e :
        raise Exception("Missing environment variable: " + str(e[0]))

    return AngelList(CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN)

def test_angel_list(al) :
    """
    Returns true if connected
    """
    if al.get_self() is not None :
        logging.info("Connected to API")
    else :
        logging.info("Could not connect to API")

    return al.get_set() is not None

def configure_logging() :
    """
    Configures logging for script
    """
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                        filename='database_entry.log',
                        filemode='w',
                        stream=sys.stdout)



al = get_angel_list()
session = get_db_session()

test_angel_list(al)
configure_logging()

def filter_hidden(data) :
    return list(filter(lambda d : not d['hidden'], data))

def get_city_data(city_id) :
    """
    Returns all city data
    """

    def clean_data(data) :
        keys = {'name', 'display_name', 'statistics'}
        missing_keys = keys - set(data.keys())

        if missing_keys :
            if 'name' in missing_keys :
                return
            logging.warn(data['name'] + " is missing keys: " + ', '.join(list(missing_keys)))

        city_stats = data['statistics']['all']

        city_data = {
                        'name': data['name'] if data['name'] else '',
                        'angel_id': data['id'],
                        'display_name': data['display_name'] if data['display_name'] else '',
                        'popularity': city_stats['followers'] if city_stats['followers'] else 0,
                        'investor_popularity': city_stats['investor_followers'] if city_stats['investor_followers'] else 0,
                        'num_companies': city_stats['startups'] if city_stats['startups'] else 0,
                        'num_people': city_stats['users'] if city_stats['users'] else 0,
                    }
        
        return city_data

    response = None
    retries = 3
    while retries and not response :
        try :
            response = al.get_tags(city_id)
            logging.info("Received response for city data of: " + str(city_id))
        except :
            logging.debug("City data response error from city: " + str(city_id))
            retries -= 1
            time.sleep(2)

    if not response or response['tag_type'] != 'LocationTag' :
        logging.debug("tag_id is not for a location: " + city_id)
        num_missed_city_data += 1
        return

    return clean_data(response)



def get_companies_by_city(city_id) :
    """
    Returns full list of company objects
    """

    def clean_data(data) :
        keys = {'name', 'logo_url', 'markets', 'locations', 'follower_count', 'product_desc'}
        missing_keys = keys - set(data.keys())

        if missing_keys :
            if 'name' in missing_keys :
                return
            logging.warn(data['name'] + " is missing keys: " + ', '.join(list(missing_keys)))

        company_data = {
                        'name': data['name'],
                        'angel_id': data['id'],
                        'logo_url': data['logo_url'] if data['logo_url']  else '',
                        'popularity': data['follower_count'] if data['follower_count'] else 0,
                        'product_desc': data['product_desc'] if data['product_desc'] else '',
                        'company_url': data['company_url'] if data['company_url'] else '',
                        'comapany_size': data['company_size'] if data['company_size'] else '',
                        }

        company_data['market'] = company_data['location'] = ''

        if data['markets'] :
            company_data['market'] = data['markets'][0]['name']

        if data['locations'] :
            company_data['location'] = data['locations'][0]['name']

        return company_data

    response = None
    retries = 3
    while retries and not response :
        try :
            response = al.get_tags_startups(city_id)
            logging.info("Recieved response for startups in: " + str(city_id))
        except :
            logging.debug("Company response error from city: " + str(city_id))
            retries -= 1
            time.sleep(2)


    if not response or 'startups' not in response :
        logging.debug("No startups in city with tag_id: " + city_id)
        num_missed_cities += 1
        return
    
    companies_data = filter_hidden(response['startups'])

    return [clean_data(company) for company in companies_data]


def get_founders_by_company(company_id) :
    """
    Returns full list of founder objects
    """
    def clean_data(data) :
        keys = {'name', 'id', 'bio', 'follower_count', 'image'}
        missing_keys = keys - set(data.keys())

        if missing_keys :
            if 'name' in missing_keys :
                return
            logging.warn(data['name'] + " is missing keys: " + ', '.join(list(missing_keys)))

        founder_data = {
                        'name': data['name'],
                        'angel_id': data['id'],
                        'bio': data['bio'] if data['bio'] else '',
                        'popularity': data['follower_count'] if data['follower_count'] else 0,
                        'image_url': data['image'] if data['image'] else '',
                        }

        return founder_data

    response = None
    retries = 3
    while retries and not response :
        try :
            response = al.get_startup_roles(startup_id=company_id, role='founder')
            logging.info("Recieved response for founders of: " + str(company_id))
        except :
            logging.debug("Startup roles response error from company: " + str(company_id))
            retries -= 1
            time.sleep(2)


    if not response or 'startup_roles' not in response :
        logging.debug("No founders found for: " + company_id)
        num_missed_founders += 1
        return

    founders_data = (f['tagged'] for f in response['startup_roles'])

    return [clean_data(founder) for founder in founders_data]


def insert_founders_by_company(founder_data, company_id, city_id) :
    founder = None
    for f in founder_data :
        founder = Founder(**f)
        if (session.query(Founder).filter(Location.angel_id == location_id).count()) == 0:

def __main__() :
    configure_logging()

    city_ids = [1692, 1664]

    all_companies = []
    all_founders = []
    all_cities = []

    # for city_id in city_ids :
    #     companies_data = get_companies_by_city(city_id)
    #     company_ids = (c['id'] for c in companies_data)
    #     all_companies += companies_data

    #     for company_id in company_ids :
    #         founders_data = get_founders_by_company(company_id)




