#!/usr/bin/env python3

# -------
# imports
# -------

from unittest import main, TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

class TestIdb(TestCase):

    engine = create_engine('sqlite:///seriesz.db')
    Session = sessionmaker(bind=engine)
    s = Session()

    # -------------
    # Founder tables
    # -------------

    def test_Founder_add_1(self):

        name = "Mark Zuckerburg"
        Startup = "Menlo Park"
        founder = True
        investor = True
        num_companies = 10
        mark = Founder(name, Startup, founder, investor, num_companies)

        s.add(mark)
        s.commit()

        mark_test = s.query(Founder).filter(Founder.name == "Mark Zuckerburg").one()
        self.assertEqual(mark, mark_test)

        s.delete(mark)
        s.commit()

    def test_Founder_query_1(self):


        name = "Mark Zuckerburg"
        Startup = "Menlo Park"
        founder = True
        investor = True
        num_companies = 10
        mark = Founder(name, Startup, founder, investor, num_companies)

        name = "Tyler Winklevoss"
        Startup = "Menlo Park"
        founder = True
        investor = True
        num_companies = 10
        tyler = Founder(name, Startup, founder, investor, num_companies)

        s.add(mark)
        s.add(tyler)
        s.commit()

        tyler_test = s.query(Founder).filter(Founder.name == "Tyler Winklevoss").one()

        self.assertEqual(tyler, tyler_test)

        s.delete(mark)
        s.delete(tyler)
        s.commit()

    def test_Founder_delete_1(self):


        name = "Mark Zuckerburg"
        Startup = "Menlo Park"
        founder = True
        investor = True
        num_companies = 10
        mark = Founder(name, Startup, founder, investor, num_companies)

        s.add(mark)
        s.commit()
        s.delete(mark)
        s.commit()

        count = session.query(Founder).filter(Founder.name == "Mark Zuckerburg").count()

        self.assertEquals(0, count)

    # ---------------
    # Founder __init__
    # ---------------

    def test_Founder_init_1(self):
        name = "Mark Zuckerburg"
        Startup = "Menlo Park"
        founder = True
        investor = True
        num_companies = 10
        Founder = Founder(name, Startup, founder, investor, num_companies)

        self.assertEqual(name, Founder.name)
        self.assertEqual(Startup, Founder.Startup)
        self.assertEqual(founder, Founder.founder)
        self.assertEqual(investor, Founder.investor)
        self.assertEqual(num_companies, Founder.num_companies)

    def test_Founder_init_2(self):
        name = ""
        Startup = ""
        founder = False
        investor = False
        num_companies = 0
        Founder = Founder(name, Startup, founder, investor, num_companies)

        self.assertEqual(name, Founder.name)
        self.assertEqual(Startup, Founder.Startup)
        self.assertEqual(founder, Founder.founder)
        self.assertEqual(investor, Founder.investor)
        self.assertEqual(num_companies, Founder.num_companies)

    def test_Founder_init_3(self):
        name = None
        Startup = None
        founder = None
        investor = None
        num_companies = None
        Founder = Founder(name, Startup, founder, investor, num_companies)

        self.assertEqual(name, Founder.name)
        self.assertEqual(Startup, Founder.Startup)
        self.assertEqual(founder, Founder.founder)
        self.assertEqual(investor, Founder.investor)
        self.assertEqual(num_companies, Founder.num_companies)

    # --------------
    # Startup tables
    # --------------

    def test_Startup_add_1(self):


        name = "Facebook"
        Startup = "Menlo Park"
        follower_count = 10
        num_investors = 10
        market = "Startup"
        facebook = Startup(name, Startup, follower_count, num_investors, market)
        s.add(facebook)
        s.commit()

        fb_test = s.query(Startup).filter(Startup.name == "Facebook").one()
        self.assertEquals(facebook, fb_test)

        s.delete(facebook)
        s.commit()

    def test_Startup_query_1(self):


        name = "Facebook"
        Startup = "Menlo Park"
        follower_count = 10
        num_investors = 10
        market = "Startup"
        facebook = Startup(name, Startup, follower_count, num_investors, market)

        name = "FB"
        Startup = "Menlo Park"
        follower_count = 10
        num_investors = 10
        market = "Startup"
        fb = Startup(name, Startup, follower_count, num_investors, market)

        s.add(facebook)
        s.add(fb)
        s.commit()

        fb_test = s.query(Startup).filter(Startup.name == "FB").one()

        self.assertEqual(fb, fb_test)

        s.delete(facebook)
        s.delete(fb)
        s.commit()

    def test_Startup_delete_1(self):


        name = "Facebook"
        Startup = "Menlo Park"
        follower_count = 10
        num_investors = 10
        market = "Startup"
        facebook = Startup(name, Startup, follower_count, num_investors, market)
        s.add(facebook)
        s.commit()
        s.delete(facebook)
        s.commit()

        count = session.query(Startup).filter(Startup.name == "Facebook").count()

        self.assertEquals(0, count)

    # ----------------
    # Startup __init__
    # ----------------

    def test_Startup_init_1(self):
        name = "Facebook"
        Startup = "Menlo Park"
        follower_count = 10
        num_investors = 10
        market = "Startup"
        Startup = Startup(name, Startup, follower_count, num_investors, market)

        self.assertEqual(name, Startup.name)
        self.assertEqual(Startup, Startup.Startup)
        self.assertEqual(follower_count, Startup.follower_count)
        self.assertEqual(num_investors, Startup.num_investors)
        self.assertEqual(market, Startup.market)

    def test_Startup_init_2(self):
        name = ""
        Startup = ""
        follower_count = 0
        num_investors = 0
        market = ""
        Startup = Startup(name, Startup, follower_count, num_investors, market)

        self.assertEqual(name, Startup.name)
        self.assertEqual(Startup, Startup.Startup)
        self.assertEqual(follower_count, Startup.follower_count)
        self.assertEqual(num_investors, Startup.num_investors)
        self.assertEqual(market, Startup.market)

    def test_Startup_init_3(self):
        name = None
        Startup = None
        follower_count = None
        num_investors = None
        market = None
        Startup = Startup(name, Startup, follower_count, num_investors, market)

        self.assertEqual(name, Startup.name)
        self.assertEqual(Startup, Startup.Startup)
        self.assertEqual(follower_count, Startup.follower_count)
        self.assertEqual(num_investors, Startup.num_investors)
        self.assertEqual(market, Startup.market)

    # ---------------
    # Startup tables
    # ---------------

    def test_location_add_1(self):


        name = "Menlo Park"
        investor_followers = 100
        followers = 1000
        num_companies = 10
        num_people = 100
        menlo = Startup(name, investor_followers, followers, num_companies, num_people)

        s.add(menlo)
        s.commit()

        menlo_test = s.query(Startup).filter(Startup.name == "Menlo Park").one()
        self.assertEqual(menlo, menlo_test)

        s.delete(menlo)
        s.commit()

    def test_location_query_1(self):


        name = "Menlo Park"
        investor_followers = 100
        followers = 1000
        num_companies = 10
        num_people = 100
        menlo = Startup(name, investor_followers, followers, num_companies, num_people)

        name = "MP"
        investor_followers = 100
        followers = 1000
        num_companies = 10
        num_people = 100
        mp = Startup(name, investor_followers, followers, num_companies, num_people)

        s.add(menlo)
        s.add(mp)
        s.commit

        mp_test = s.query(Startup).filter(Startup.name == "MP").one()

        self.assertEqual(mp, mp_test)

        s.delete(mp)
        s.delete(menlo)
        s.commit()

    def test_location_delete_1(self):


        name = "Menlo Park"
        investor_followers = 100
        followers = 1000
        num_companies = 10
        num_people = 100
        menlo = Startup(name, investor_followers, followers, num_companies, num_people)

        s.add(menlo)
        s.commit()
        s.delete(menlo)
        s.commit()

        count = session.query(Startup).filter(Startup.name == "Menlo Park").count()

        self.assertEquals(0, count)
    # -----------------
    # Startup __init__
    # -----------------

    def test_location_init_1(self):
        name = "Menlo Park"
        investor_followers = 100
        followers = 1000
        num_companies = 10
        num_people = 100
        Startup = Startup(name, investor_followers, followers, num_companies, num_people)

        self.assertEqual(name, Startup.name)
        self.assertEqual(investor_followers, Startup.investor_followers)
        self.assertEqual(followers, Startup.followers)
        self.assertEqual(num_companies, Startup.num_companies)
        self.assertEqual(num_people, Startup.num_people)

    def test_location_init_2(self):
        name = ""
        investor_followers = 0
        followers = 0
        num_companies = 0
        num_people = 0
        Startup = Startup(name, investor_followers, followers, num_companies, num_people)

        self.assertEqual(name, Startup.name)
        self.assertEqual(investor_followers, Startup.investor_followers)
        self.assertEqual(followers, Startup.followers)
        self.assertEqual(num_companies, Startup.num_companies)
        self.assertEqual(num_people, Startup.num_people)

    def test_location_init_3(self):
        name = None
        investor_followers = None
        followers = None
        num_companies = None
        num_people = None
        Startup = Startup(name, investor_followers, followers, num_companies, num_people)

        self.assertEqual(name, Startup.name)
        self.assertEqual(investor_followers, Startup.investor_followers)
        self.assertEqual(followers, Startup.followers)
        self.assertEqual(num_companies, Startup.num_companies)
        self.assertEqual(num_people, Startup.num_people)

# ----
# main
# ----

if __name__ == "__main__":
    main()
