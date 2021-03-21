#import dependencies
from flask import Flask, jsonify,render_template
import numpy as np
import sqlalchemy
import psycopg2
from config import user, password
from sqlalchemy import inspect, create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import text

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

    quotes_all = engine.execute("Select quotes.author_name, quotes.text, quotes.quote_id from quotes").fetchall()
    
    quotes_list = []
    for items in quotes_all:
        quotes_dict = {}
        quotes_dict['author'] = items[0]
        quotes_dict['text'] = items[1]  
        quote_id_str=str(items[2])

        query3=text("select Quote_tags.tag from Quote_tags where Quote_tags.quote_id=\'"+quote_id_str.replace('\'','\'\'')+"\'")
        quote_data = engine.execute(query3).fetchall()
            
        tags_list = []
        for tags in quote_data:
            tags_list.append(tags[0])
            
        quotes_dict['tags'] = tags_list
        quotes_list.append(quotes_dict)
            
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

        author_quotes = engine.execute("select quotes.text, quotes.quote_id from quotes where quotes.author_name=\'"+items[0].replace('\'','\'\'')+"\'").fetchall()

        quotes_list= []
        for quotes in author_quotes:
            quotes_dict = {}
            quotes_dict['text'] = quotes[0]
            quote_id_str=str(quotes[1])

            query3=text("select Quote_tags.tag from Quote_tags where Quote_tags.quote_id=\'"+quote_id_str.replace('\'','\'\'')+"\'")
            quote_data = engine.execute(query3).fetchall()
            
            tags_list = []
            for tags in quote_data:
               tags_list.append(tags[0])
            
            quotes_dict['tags'] = tags_list
            quotes_list.append(quotes_dict)
        
        authors_dict['quotes'] = quotes_list
        authors_list.append(authors_dict)

    return (jsonify({'details': authors_list, 'count': len(authors_list)}))

    session.close()

@app.route('/authors/<author_name>')
def authors2(author_name):
    session = Session(engine)
    query = text("Select author.author_name,author.born,author.description,quotesCount.quotes_count \
        from author join (select count(*) as quotes_count, quotes.author_name from quotes group by quotes.author_name) as quotesCount \
            on author.author_name = :author_name and \
            quotesCount.author_name = author.author_name \
            order by quotesCount.quotes_count desc")
    author_all = engine.execute(query, {'author_name': author_name})
    
    ### authors_list = []
    for items in author_all:
        authors_dict = {}
        authors_dict['name'] = items[0]
        ### authors_dict['born'] = items[1]
        authors_dict['description'] = items[2]
        authors_dict['number_of_quotes'] = items[3]

        query2=text("select quotes.text, quotes.quote_id from quotes where quotes.author_name=\'"+items[0].replace('\'','\'\'')+"\'")
        author_quotes = engine.execute(query2).fetchall()
        
        quotes_list= []
        for quotes in author_quotes:
            quotes_dict = {}
            quotes_dict['text'] = quotes[0]
            quote_id_str=str(quotes[1])

            query3=text("select Quote_tags.tag from Quote_tags where Quote_tags.quote_id=\'"+quote_id_str.replace('\'','\'\'')+"\'")
            quote_data = engine.execute(query3).fetchall()
            
            tags_list = []
            for tags in quote_data:
               tags_list.append(tags[0])
            
            quotes_dict['tags'] = tags_list
            quotes_list.append(quotes_dict)
            
        authors_dict['quotes'] = quotes_list
        authors_list = authors_dict

    return (jsonify(authors_list))

    session.close()

@app.route('/tags')
def all_tags():
    session = Session(engine)

    tags_1 = engine.execute("select quote_tags.tag, count(*) from quote_tags group by quote_tags.tag order by count(quote_tags.tag) desc, quote_tags.tag").fetchall()

    allTag_list = []
    for items in tags_1:
        allTag_dict = {}
        allTag_dict['name'] = items[0]
        allTag_dict['number_pf_quotes'] = items[1]

        tag_quotes= engine.execute("select quotes.text,quote_tags.tag from quotes join quote_tags on quotes.quote_id=quote_tags.quote_id where quote_tags.tag =\'"+items[0]+"\'").fetchall()
        quotes_list = []
        for quote in tag_quotes:
            quotes_dict = {}
            quotes_dict['text'] = quote[0]

            quote_tags = engine.execute("select quote_tags.tag from quote_tags join quotes on quotes.quote_id=quote_tags.quote_id where quotes.text =\'"+quote[0].replace('\'','\'\'')+"\'").fetchall()
            #print(quote_tags)
            tag_list=[]
            for tag in quote_tags:
                tag_list.append(tag[0])

            quotes_dict['tags'] = tag_list

            quotes_list.append(quotes_dict)

        allTag_dict['quotes'] = quotes_list


        allTag_list.append(allTag_dict)
        
    #final_quotes_list = ['quotes': quotes_list]
    return (jsonify({'details': allTag_list, 'count': len(allTag_list)}))

    session.close()

@app.route('/tags/<tags>')
def tags1(tags):
    session = Session(engine)

    tag_quotes= engine.execute("select quotes.text,quote_tags.tag from quotes join quote_tags on quotes.quote_id=quote_tags.quote_id where quote_tags.tag =\'"+tags+"\'").fetchall()
    
    quotes_list = []
    for quote in tag_quotes:
        quotes_dict = {}
        quotes_dict['text'] = quote[0]

        quote_tags = engine.execute("select quote_tags.tag from quote_tags join quotes on quotes.quote_id=quote_tags.quote_id where quotes.text =\'"+quote[0].replace('\'','\'\'')+"\'").fetchall()
        #print(quote_tags)
        tag_list=[]
        for tag in quote_tags:
            tag_list.append(tag[0])

        quotes_dict['tags'] = tag_list

        quotes_list.append(quotes_dict)
        
    #final_quotes_list = ['quotes': quotes_list]
    return (jsonify({'details': quotes_list, 'count': len(quotes_list)}))

    session.close()






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
        
    return jsonify(top_list)

    session.close()




if __name__ == "__main__":
    app.run(debug=True)