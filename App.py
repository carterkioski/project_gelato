#import dependencies
from flask import Flask, jsonify,render_template
import numpy as np
import sqlalchemy
import psycopg2
from config import user, password
from sqlalchemy import inspect, create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

engine = create_engine(f'postgresql://{user}:{password}@localhost:5432/Quotes_to_Scrape_DB') 
connection = engine.connect()
#Reflect an existing database and tables
Base = automap_base()
Base.prepare(engine, reflect=True)

#Save reference to the tables
Authors = Base.classes.author
Quotes = Base.classes.quotes
Quote_tags = Base.classes.quote_tags


#creating an app
app = Flask(__name__)

#Homepage
@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/quotes')
def all_quotes():
    session = Session(engine)

    quotes_all = engine.execute("Select quotes.author_name, quotes.text from quotes").fetchall()

    
    quotes_list = []
    for items in quotes_all:
        quotes_dict = {}
        quotes_dict['author'] = items[0]
        quotes_dict['text'] = items[1]
        quotes_list.append(quotes_dict)
        
    #final_quotes_list = ['quotes': quotes_list]
    return (jsonify({'quotes': quotes_list, 'total': len(quotes_list)}))

    session.close()



@app.route('/authors')
def all_authors():
    session = Session(engine)

    author_all = engine.execute("Select author.author_name,author.born,author.description,quotesCount.quotes_count \
        from author join (select count(*) as quotes_count, quotes.author_name from quotes group by quotes.author_name) as quotesCount on quotesCount.author_name = author.author_name \
            order by quotesCount.quotes_count desc").fetchall()

    
    authors_list = []
    for items in author_all:
        authors_dict = {}
        authors_dict['name'] = items[0]
        authors_dict['born'] = items[1]
        authors_dict['description'] = items[2]
        authors_dict['count'] = items[3]

        author_quotes = engine.execute("select quotes.text from quotes where quotes.author_name=\'"+items[0].replace('\'','\'\'')+"\'").fetchall()

        quotes_list= []
        for quotes in author_quotes:
            quotes_dict = {}
            quotes_dict['text'] = quotes[0]
            quotes_list.append(quotes_dict)

        authors_dict['quotes'] = quotes_list

        authors_list.append(authors_dict)

    return (jsonify({'details': authors_list, 'count': len(authors_list)}))

    session.close()

#@app.route('/authors/<authour%name>')
# def authors2(author_name):

# @app.route('/tags')
# def all_tags():



# @app.route('/tags/<tags>')
# def tags1(tag):


@app.route('/top10tags')
def top_tags():
    session = Session(engine)

    top_tags = engine.execute("select quote_tags.tag, count(*) from quote_tags group by quote_tags.tag order by count(quote_tags.tag) desc, quote_tags.tag limit 10").fetchall()

    
    top_list = []
    for items in top_tags:
        top_dict = {}
        top_dict['tags'] = items[0]
        top_dict['total'] = items[1]
        top_list.append(top_dict)
        
    #final_quotes_list = ['quotes': quotes_list]
    return jsonify(top_list)

    session.close()




if __name__ == "__main__":
    app.run(debug=True)