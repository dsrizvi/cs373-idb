# create_db.py

from app import db
from models import Person


# def create_db:
db.create_all()

# def create_dummy_data:
# person = Person(
# 	name = "Mark Zuckerburge"
#     location = "Menlo park"
#     founder = True
#     investor = True
#     num_companies = 1
#     image = "Mark Zuckerburge"
#     bio = "A Harvard dropout"
# )


# db.session.add(person)
# db.session.commit()
