# config.py


import os


class BaseConfig(object):
    SECRET_KEY = '(15ds+i2+%ik6z&!yer+ga9m=e%jcqiz_5wszg)r-z!2--b2d'
    DEBUG = False
    DB_NAME = 'postgres'
    DB_USER = 'postgres'
    DB_PASS = 'postgres'
    DB_SERVICE = 'postgres'
    DB_PORT = 5432
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
    )


# class BaseConfig(object):
#     SECRET_KEY = 'hi'
#     DEBUG = True
#     DB_NAME = 'postgres'
#     DB_SERVICE = 'localhost'
#     DB_PORT = 5432
#     SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}/{2}'.format(
#         DB_SERVICE, DB_PORT, DB_NAME
#     )