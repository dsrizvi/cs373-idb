# app.py


from flask import Flask
from flask import request, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from config import BaseConfig

#for running tests
from io import StringIO
import tests
from unittest import TextTestRunner, makeSuite


app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)


from models import *


@app.route('/', methods=['GET', 'POST'])
def index():
    # if request.method == 'POST':
    #     text = request.form['text']
    #     post = Post(text)
    #     db.session.add(post)
    #     db.session.commit()
    # posts = Post.query.all()
    return render_template('index.html')

@app.route('/tests', methods=['GET'])
def run_tests():
    """
    output: returns the output of unittests
    """
    
    stream = StringIO()
    runner = TextTestRunner(stream=stream, verbosity=2)
    suite = makeSuite(tests.TestIDB)
    runner.run(suite)
    output = stream.getvalue().output.split('\n')
    return render_template("tests.html", text=output)


if __name__ == '__main__':
    app.run()
