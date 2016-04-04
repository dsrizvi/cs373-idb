import logging
import os

from flask import Flask, render_template, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from models import Base, Person

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
logger.debug("Welcome to Carina Guestbook")


SQLALCHEMY_DATABASE_URI = \
    '{engine}://{username}:{password}@{hostname}/{database}'.format(
        engine='mysql+pymysql',
        username=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        hostname=os.getenv('MYSQL_HOST'),
        database=os.getenv('MYSQL_DATABASE'))

logger.debug("The log statement below is for educational purposes only. Do *not* log credentials.")
logger.debug("%s", SQLALCHEMY_DATABASE_URI)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    logger.debug("index")

    if request.method == 'POST':
        name = request.form['name']
        guest = Guest(name=name)
        db.session.add(guest)
        db.session.commit()
        return redirect(url_for('index'))


    print(Person.query.all())
    return render_template('index.html', guests=Person.query.all())


# class Guest(db.Model):
#     __tablename__ = 'guests'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(256), nullable=False)

#     def __repr__(self):
#         return "[Guest: id={}, name={}]".format(self.id, self.name)



if __name__ == '__main__':
    manager.run()
