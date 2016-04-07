#!/usr/bin/env python3

# -------
# imports
# -------

from unittest import main, TestCase

from models import Person, Company, Location, Connection

class TestIdb(TestCase):
 
    # -------------
    # Person tables
    # -------------

    def test_person_add_1(self):
        s = session()
        
        name = "Mark Zuckerburg"
        location = "Menlo Park"
        founder = True
        investor = True
        num_companies = 10
        mark = Person(name, location, founder, investor, num_companies)
 
        s.add(mark)
        s.commit()

        mark_test = s.query(Person).filter(Person.name == "Mark Zuckerburg").one()
        self.assertEqual(mark, mark_test)

        s.delete(mark)
        s.commit()

    def test_person_query_1(self):
        s = session()

        name = "Mark Zuckerburg"
        location = "Menlo Park"
        founder = True
        investor = True
        num_companies = 10
        mark = Person(name, location, founder, investor, num_companies)

        name = "Tyler Winklevoss"
        location = "Menlo Park"
        founder = True
        investor = True
        num_companies = 10
        tyler = Person(name, location, founder, investor, num_companies) 

        s.add(mark)
        s.add(tyler)
        s.commit()
        
        tyler_test = s.query(Person).filter(Person.name == "Tyler Winklevoss").one()        

        self.assertEqual(tyler, tyler_test)

        s.delete(mark)
        s.delete(tyler)
        s.commit()

    def test_person_delete_1(self):
        s = session()

        name = "Mark Zuckerburg"
        location = "Menlo Park"
        founder = True
        investor = True
        num_companies = 10
        mark = Person(name, location, founder, investor, num_companies)

        s.add(mark)
        s.commit()
        s.delete(mark)
        s.commit()

        count = session.query(Person).filter(Person.name == "Mark Zuckerburg").count() 

        self.assertEquals(0, count)        

    # ---------------
    # Person __init__
    # ---------------

    def test_person_init_1(self):
        name = "Mark Zuckerburg"
        location = "Menlo Park"
        founder = True
        investor = True
        num_companies = 10
        person = Person(name, location, founder, investor, num_companies)
        
        self.assertEqual(name, person.name)
        self.assertEqual(location, person.location)
        self.assertEqual(founder, person.founder)
        self.assertEqual(investor, person.investor)
        self.assertEqual(num_companies, person.num_companies)

    def test_person_init_2(self):
        name = ""
        location = ""
        founder = False
        investor = False
        num_companies = 0
        person = Person(name, location, founder, investor, num_companies)

        self.assertEqual(name, person.name)
        self.assertEqual(location, person.location)
        self.assertEqual(founder, person.founder)
        self.assertEqual(investor, person.investor)
        self.assertEqual(num_companies, person.num_companies) 
 
    def test_person_init_3(self):
        name = None
        location = None
        founder = None
        investor = None
        num_companies = None
        person = Person(name, location, founder, investor, num_companies)

        self.assertEqual(name, person.name)
        self.assertEqual(location, person.location)
        self.assertEqual(founder, person.founder)
        self.assertEqual(investor, person.investor)
        self.assertEqual(num_companies, person.num_companies)
    
    # --------------
    # Company tables
    # --------------

    def test_company_add_1(self):
        s = session()
        
        name = "Facebook"
        location = "Menlo Park"
        follower_count = 10
        num_investors = 10
        market = "Startup"
        facebook = Company(name, location, follower_count, num_investors, market) 
        s.add(facebook)
        s.commit()

        fb_test = s.query(Company).filter(Company.name == "Facebook").one()
        self.assertEquals(facebook, fb_test)

        s.delete(facebook)
        s.commit()

    def test_company_query_1(self):
        s = session()

        name = "Facebook"
        location = "Menlo Park"
        follower_count = 10
        num_investors = 10
        market = "Startup"
        facebook = Company(name, location, follower_count, num_investors, market)
        
        name = "FB"
        location = "Menlo Park"
        follower_count = 10
        num_investors = 10
        market = "Startup"
        fb = Company(name, location, follower_count, num_investors, market)
        
        s.add(facebook)
        s.add(fb)
        s.commit()

        fb_test = s.query(Company).filter(Company.name == "FB").one()

        self.assertEqual(fb, fb_test)

        s.delete(facebook)
        s.delete(fb)
        s.commit()

    def test_company_delete_1(self):
        s = session()

        name = "Facebook"
        location = "Menlo Park"
        follower_count = 10
        num_investors = 10
        market = "Startup"
        facebook = Company(name, location, follower_count, num_investors, market)
        s.add(facebook)
        s.commit()
        s.delete(facebook)
        s.commit()

        count = session.query(Company).filter(Company.name == "Facebook").count()
    
        self.assertEquals(0, count)

    # ----------------
    # Company __init__
    # ----------------

    def test_company_init_1(self):
        name = "Facebook"
        location = "Menlo Park"
        follower_count = 10
        num_investors = 10
        market = "Startup"
        company = Company(name, location, follower_count, num_investors, market)

        self.assertEqual(name, company.name)
        self.assertEqual(location, company.location)
        self.assertEqual(follower_count, company.follower_count)
        self.assertEqual(num_investors, company.num_investors)
        self.assertEqual(market, company.market)

    def test_company_init_2(self):
        name = ""
        location = ""
        follower_count = 0
        num_investors = 0
        market = ""
        company = Company(name, location, follower_count, num_investors, market)

        self.assertEqual(name, company.name)
        self.assertEqual(location, company.location)
        self.assertEqual(follower_count, company.follower_count)
        self.assertEqual(num_investors, company.num_investors)
        self.assertEqual(market, company.market)
 
    def test_company_init_3(self):
        name = None
        location = None
        follower_count = None
        num_investors = None
        market = None
        company = Company(name, location, follower_count, num_investors, market)

        self.assertEqual(name, company.name)
        self.assertEqual(location, company.location)
        self.assertEqual(follower_count, company.follower_count)
        self.assertEqual(num_investors, company.num_investors)
        self.assertEqual(market, company.market)

    # ---------------
    # Location tables
    # ---------------

    def test_location_add_1(self):
        s = session()        

        name = "Menlo Park"
        investor_followers = 100
        followers = 1000
        num_companies = 10
        num_people = 100
        menlo = Location(name, investor_followers, followers, num_companies, num_people)
    
        s.add(menlo)
        s.commit()

        menlo_test = s.query(Location).filter(Location.name == "Menlo Park").one()
        self.assertEqual(menlo, menlo_test)

        s.delete(menlo)
        s.commit()    

    def test_location_query_1(self):
        s = session()

        name = "Menlo Park"
        investor_followers = 100
        followers = 1000
        num_companies = 10
        num_people = 100
        menlo = Location(name, investor_followers, followers, num_companies, num_people)

        name = "MP"
        investor_followers = 100
        followers = 1000
        num_companies = 10
        num_people = 100
        mp = Location(name, investor_followers, followers, num_companies, num_people)     

        s.add(menlo)
        s.add(mp)
        s.commit

        mp_test = s.query(Location).filter(Location.name == "MP").one()

        self.assertEqual(mp, mp_test)

        s.delete(mp)
        s.delete(menlo)
        s.commit()

    def test_location_delete_1(self):
        s = session()

        name = "Menlo Park"
        investor_followers = 100
        followers = 1000
        num_companies = 10
        num_people = 100
        menlo = Location(name, investor_followers, followers, num_companies, num_people)

        s.add(menlo)
        s.commit()
        s.delete(menlo)
        s.commit()

        count = session.query(Location).filter(Location.name == "Menlo Park").count()

        self.assertEquals(0, count)        
    # -----------------
    # Location __init__
    # -----------------

    def test_location_init_1(self):
        name = "Menlo Park"
        investor_followers = 100
        followers = 1000
        num_companies = 10
        num_people = 100
        location = Location(name, investor_followers, followers, num_companies, num_people)

        self.assertEqual(name, company.name)
        self.assertEqual(investor_followers, company.investor_followers)
        self.assertEqual(followers, company.followers)
        self.assertEqual(num_companies, company.num_companies)
        self.assertEqual(num_people, company.num_people) 

    def test_location_init_2(self):
        name = ""
        investor_followers = 0
        followers = 0
        num_companies = 0
        num_people = 0
        location = Location(name, investor_followers, followers, num_companies, num_people)

        self.assertEqual(name, company.name)
        self.assertEqual(investor_followers, company.investor_followers)
        self.assertEqual(followers, company.followers)
        self.assertEqual(num_companies, company.num_companies)
        self.assertEqual(num_people, company.num_people)

    def test_location_init_3(self):
        name = None
        investor_followers = None
        followers = None
        num_companies = None
        num_people = None
        location = Location(name, investor_followers, followers, num_companies, num_people)

        self.assertEqual(name, company.name)
        self.assertEqual(investor_followers, company.investor_followers)
        self.assertEqual(followers, company.followers)
        self.assertEqual(num_companies, company.num_companies)
        self.assertEqual(num_people, company.num_people) 

# ----
# main
# ----

if __name__ == "__main__":
    main()
