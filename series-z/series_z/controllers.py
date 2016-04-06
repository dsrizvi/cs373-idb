import os

from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory
from flask import send_file, make_response, abort

from series_z import app

# routing for API endpoints, generated from the models designated as API_MODELS
from series_z.core import api_manager
from series_z.models import *

for model_name in app.config['API_MODELS']:
    model_class = app.config['API_MODELS'][model_name]
    api_manager.create_api(model_class, methods=['GET', 'POST'])

session = api_manager.session


# routing for basic pages (pass routing onto the Angular app)
@app.route('/')
@app.route('/about')
@app.route('/blog')
def basic_pages(**kwargs):
    return make_response(open('series_z/templates/index-b.html').read())


# routing for CRUD-style endpoints
# passes routing onto the angular frontend if the requested resource exists
from sqlalchemy.sql import exists

crud_url_models = app.config['CRUD_URL_MODELS']

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

@app.route('/<model_name>/<item_id>')
def rest_pages(model_name, item_id=None):
    if model_name in crud_url_models:
        model_class = crud_url_models[model_name]
        if item_id is None or session.query(exists().where(
                model_class.id == item_id)).scalar():
            return make_response(open(
                'series_z/templates/index-b.html').read())
    abort(404)


# special file handlers and error handlers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/favicon.ico')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
