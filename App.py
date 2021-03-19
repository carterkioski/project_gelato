#import dependencies
from flask import Flask, jsonify,render_template
import numpy as np
import sqlalchemy
import datetime as dt
from sqlalchemy import inspect, create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session





#creating an app
app = Flask(__name__)

#Homepage
@app.route('/')
def home_page():
    return render_template('index.html')

#@app.route('/quotes')
#def all_quotes():

#@app.route('/authors')
#def all_authors():

#@app.route('/authors/<authour%name>')
# def authors2(author_name):

# @app.route('/tags')
# def all_tags():



# @app.route('/tags/<tags>')
# def tags1(tag):


# @app.route('/top10tags')
# def top_tags():



if __name__ == "__main__":
    app.run(debug=True)
