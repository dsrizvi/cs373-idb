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

from sqlalchemy import create_engine, exists
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine('sqlite:///seriesz.db')
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
            print item.__dict__
            return render_template('founder.html')
        except :
            print sys.exc_info()[0]
            return render_template('index-b.html')

    if model_name == 'startups' :
        try :
            item = db_session.query(Startup).get(item_id)
            return render_template('startup.html')
        except :
            print sys.exc_info()[0]
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
@app.route('/api/startups/<int:id_>', methods=['GET'])
def api_startups(id):
    startup = Startup.query.filter(Startup.id == id_).one_or_none().__dict__

    return json.dumps(startup)


################ Danyal end   ################


def runserver():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    runserver()