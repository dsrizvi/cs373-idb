import os, sys
import json
from flask import Flask, request, Response
from flask import render_template, send_from_directory, url_for, redirect, send_file, make_response, abort

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

from sqlalchemy.sql import exists

from models import *


app = Flask(__name__)

app.url_map.strict_slashes = False
db = SQLAlchemy(app)
api_manager = APIManager(app, flask_sqlalchemy_db=db)
session = api_manager.session


app.config.update(
    PROPAGATE_EXCEPTIONS = True
)

from sqlalchemy import create_engine, exists
from sqlalchemy.orm import scoped_session, sessionmaker


URI = 'postgresql://postgres:postgres@146.20.68.107/postgres'
engine = create_engine(URI)
Session = sessionmaker(bind=engine)
db_session = Session()

@app.route('/')
@app.route('/about')
def basic_pages(**kwargs):
    return make_response(open('templates/index-b.html').read())



@app.route('/<model_name>/')
def show_model_page(model_name):

    if model_name == 'cities' :
        data = [f.__dict__ for f in db_session.query(City).all()]
        return render_template("city_listing.html", cities=data)

    if model_name == 'founders' :
        data = [f.__dict__ for f in db_session.query(Founder).all()]
        return render_template("founder_listing.html", founders=data)

    if model_name == 'startups' :
        data = [f.__dict__ for f in db_session.query(Startup).all()]
        return render_template("startup_listing.html", startups=data)

    return render_template('404.html')


@app.route('/<model_name>/<item_id>')
def show_item_page(model_name, item_id):
    if model_name == 'cities' :
        try :
            item = db_session.query(City).get(item_id)
            return render_template('city.html')
        except :
            return render_template('index-b.html')

    if model_name == 'founders' :
        try :
            item = db_session.query(Founder).get(item_id)
            return render_template('founder.html')
        except :
            return render_template('index-b.html')

    if model_name == 'startups' :
        try :
            item = db_session.query(Startup).get(item_id)
            return render_template('startup.html')
        except :
            return render_template('index-b.html')


    return render_template('404.html')


# special file handlers and error handlers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/favicon.ico')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

################ Danyal start ################

@app.route('/api/startups', methods=['GET'])
def api_startups():

    startups = db_session.query(City).all()
    data = []

    for startup in startups:
        data.append(row_dict(startup))

    data = json.dumps(data)

    return data

@app.route('/api/startup/<int:id>', methods=['GET'])
def api_startup(id):
    startup = db_session.query(Startup).get(id)

    if startup:
        startup = row_dict(startup)
        data = json.dumps(startup, ensure_ascii=False)
    else:
        data = ''

    return data

@app.route('/api/founders', methods=['GET'])
def api_founders():

    founders = db_session.query(Founder).all()
    data = []
    for founder in founders:
        data.append(row_dict(founder))

    data = json.dumps(data)

    return data


@app.route('/api/founder/<int:id>', methods=['GET'])
def api_founder(id):
    founder = db_session.query(Founder).get(id)

    if founder:
        founder = row_dict(founder)
        data = json.dumps(founder, ensure_ascii=False)
    else:
        data = ''

    return data

@app.route('/api/cities', methods=['GET'])
def api_cities():
    cities = db_session.query(City).all()
    data = []
    for city in cities:
        data.append(row_dict(city))

    data = json.dumps(data)

    return data


@app.route('/api/city/<int:id>', methods=['GET'])
def api_city(id):
    city = db_session.query(City).get(id)

    if city:
        city = row_dict(city)
        data = json.dumps(city, ensure_ascii=False)
    else:
        data = ''


    return data

def row_dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d


################ Danyal end   ################


def runserver():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

if __name__ == '__main__':
    runserver()