from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
import logging
from config import BaseConfig
import models
from models import Base


logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

SQLALCHEMY_DATABASE_URI = BaseConfig.SQLALCHEMY_DATABASE_URI
logger.debug(SQLALCHEMY_DATABASE_URI)


engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True, echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

# Base = declarative_base()
# Base.query = db_session.query_property()

def init_db():
  # import all modules here that might define models so that
  # they will be registered properly on the metadata.  Otherwise
  # you will have to import them first before calling init_db()
  Base.metadata.create_all(bind=engine)
  # logger.debug("Models created.")


if __name__ == '__main__':
  init_db()