import os
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


# routing for basic pages (pass routing onto the Angular app)
@app.route('/')
@app.route('/about')
@app.route('/blog')
def basic_pages(**kwargs):
    return make_response(open('templates/index-b.html').read())


# routing for CRUD-style endpoints
# passes routing onto the angular frontend if the requested resource exists

data =  {
            'startups' : [
                {
                    'name': 'Slack',
                    'location': 'San Francisco',
                    'founders': ['Stewart Butterfield'],
                    'popularity': 50,
                    'investors': 6,
                    'market': 'Productivity'
                },
                {
                    'name': 'Uber',
                    'location': 'San Francisco',
                    'founders': ['Travis Kalanik'],
                    'popularity': 50,
                    'investors': 6,
                    'market': 'Transportation'
                },
                {
                    'name': 'Palantir Technologies',
                    'location': 'San Francisco',
                    'founders': ['Alex Karp'],
                    'popularity': 50,
                    'investors': 6,
                    'market': 'Data Analytics'
                }
            ],

            'people' : [
                {
                    'name': 'Stewart Butterfield',
                    'location': 'San Francisco',
                    'founder': True,
                    'investor': False,
                    'companies': 3
                },
                {
                    'name': 'Alex Karp',
                    'location': 'San Francisco',
                    'founder': True,
                    'investor': False,
                    'companies': 3
                },
                {
                    'name': 'John Smith',
                    'location': 'San Francisco',
                    'founder': False,
                    'investor': True,
                    'companies': 3
                }
            ],

            'cities' : [
                {
                    'name': 'San Francisco',
                    'popularity': 39,
                    'investors': 231,
                    'founders': 234,
                    'companies': 124,
                },
                {
                    'name': 'Austin',
                    'popularity': 39,
                    'investors': 231,
                    'founders': 234,
                    'companies': 124,
                },
                {
                    'name': 'New York',
                    'popularity': 39,
                    'investors': 231,
                    'founders': 234,
                    'companies': 124,
                }

            ]
        }


@app.route('/<model_name>/')
def show_model_page(model_name):
    return render_template('listing.html', model_name=model_name.capitalize(), data=data[model_name])


# special file handlers and error handlers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/favicon.ico')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404




def runserver():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    runserver()