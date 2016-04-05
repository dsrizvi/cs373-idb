from angel import angel
import time

CLIENT_ID = 'f4bc189150f55e3a4e04d7dd47d6f60d5d0101b7c16c9719'
CLIENT_SECRET = '45e8cf40afa601846ea9af9dcf4d101aef2d183514690433'
ACCESS_TOKEN = '7b2f970c65843c003f29faab3cd089d9a2fe65fb738a1f69'
al = angel.AngelList(CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN)

def scrape():
	region_ids = []
	region_ids.append(1692)
	region_ids.append(1664)
	num_ids = 100
	company_ids = get_company_ids(region_ids, num_ids)	

    for company_id in company_ids:
        #query table for company to see if already existing
        company = al.get_startup(company_id)
		#not sure what get_startup returns if there's no company for id....
        if company not None and not company['hidden']:
            enter_company(company)
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
    if location DNE:
        location_tag = al.get_tags(location_id)
        enter_location(location_tag)

    #upload company to Company table (make sure to include location_id)


def enter_location(location):
    name = location['name']
    investor_followers = location['statistics']['all']['investor_followers']
    followers = location['statistics']['all']['followers']
    num_companies = 0
    num_people = 0

    #upload location to Location table

def enter_user(user):
    name = user['name']
    #ACCOUNT FOR NO LOCATION
    location = user['locations'][0]['name']
    founder = False
    investor = False
    num_companies = 0
    image = user['image']
    bio = user['bio']

    #upload user to Person table

def enter_connections(company):
    founders = al.get_startup_roles(startup_id=company['id'], role=['founder'])
    investors = al.get_startup_roles(startup_id=company['id'], role=['past_investor'])
    enter_founder_investors(founders, company)
    enter_founder_investors(investors, company)

#not positive about the logic in this function
def enter_founder_investors(roles, company):
    role_list = roles['startup_roles']
    for role in role_list:
        if role['tagged']['type'] == "User":
           	#query table for User name
           	if user DNE:
           		user = al.get_user(role['tagged']['id'])
            	enter_user(user)
            
			if role['role'] == "founder":
				isInvestor = False
			else:
				isInvestor = True
            person_id = role['tagged']['id']
            company_id = company['id']
 			#upload connection into Connection table
		
		if role['tagged']['type'] == "Startup":
			#query table for Company name
            if company DNE:
            	comp = al.get_startup(role['tagged']['id'])
            	enter_company(comp)
            investor_id = role['tagged']['id']
            company_id = company['id']
			#upload investment into Investment table
			
def get_company_ids(region_ids, num_ids):
	"""
	region_ids: a list of ids for regions from which you want company ids
	num_ids: the max number of company ids you want from each region
	"""

	startup_ids = []

	for r_id in region_ids:
		startups = al.get_tags_startups(r_id)
		count = 0
        for startup in startups:
            if count >= num_ids:
                break
            startup_ids.append(startup['id'])
            count += count
    
