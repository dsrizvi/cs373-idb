import os
import json
from flask import Flask, request, Response
from flask import render_template, send_from_directory, url_for, redirect, send_file, make_response, abort

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

from models import *
from sqlalchemy import create_engine, exists
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

app.config.from_object('settings')
app.url_map.strict_slashes = False

db = SQLAlchemy(app)

api_manager = APIManager(app, flask_sqlalchemy_db=db)


def get_db_session() :
    engine = create_engine('sqlite:///seriesz.db')

    engine = create_engine('sqlite:///seriesz.db')
    Session = sessionmaker(bind=engine)
    s = Session()

    return s
# for model_name in app.config['API_MODELS']:
#     model_class = app.config['API_MODELS'][model_name]
#     api_manager.create_api(model_class, methods=['GET', 'POST'])

session = api_manager.session

s = get_db_session()

# routing for basic pages (pass routing onto the Angular app)
@app.route('/')
@app.route('/about')
def basic_pages(**kwargs):
    return make_response(open('templates/index-b.html').read())


@app.route('/<model_name>/')
def show_model_page(model_name):
    data = [f.__dict__ for f in s.query(City).all()]
    return render_template('listing.html', model_name=model_name.capitalize(), data=data)

@app.route('/<model_name>/<id>')
def show_single_page(model_name, id):
    return render_template('single-page.html')



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
