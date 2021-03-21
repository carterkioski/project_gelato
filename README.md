# Project 2 - Team Gelato - ETL Project


## Overview

This project integrates numerous technologies such as: Screen Scraping with Splinter and BeautifulSoup; NoSql database storage of the scraped data using Mongo; ETL using Python, SQL, SQlAlchemy and Postgres; and Postgres backend, Python / Flask application and HTML front end to present the results. 

* Included in this submission are several folders:  
   
  * Code: Contains jupyter notebook with screen scraping code and final python/flask app.  

  * Database: SQL code for creating the Postgres database tables and 2 ETL steps for creating a clean quote_tags table.

  * Documentation: ERD word document and ETL steps taken. 

  * Resources: Contains the 3 csv files that are loaded into the Postsgres database, and 1 staging table used in the ETL process to create the final quote_tags table.  
  

## Files

* [Code:](Code)  

  * [Jupyter Notebook for Scraping](Code/scrape_final.ipynb)- scrapes quotes.toscrape.com and genrates 3 collections in Mongo.

  * [Jupyter Notebook for Ed's PC to run Scraping](Code/scrape_final_Eds-PC.ipynb)- version of same code above that has workaround for installing ChromeDriverManager for Ed's PC that has a bug.  

  * [App for running the Python/Flask code to display query data](Code/app_final.py)- Routes for 6 queries against the postgres database.  


* [Database:](Database)
  
  * [Schema exported from QuickDBD](Database/QuickDBD-export-Postgress-schema-Final.sql) - SQL exported from the ERD tool, but manually changed to remove all ".

  * [ETL-1 - Initalize Staging Table for Quote_Tags](Database/ETL-1-Schema_for_Initializing_Quote_Tags.sql) - SQL to create staging table with quotes and tag, so a merge can be done to create the table with quote_id.
  
  * [ETL-2 - Creates the final quote_tag data](Database/ETL-2-Populate_Quote_Tags.sql) - SQL to join the staging table created in ETL-1 with quotes table data to add quote_id and insert the quote_id and tag into the with quote_tag table.  


* [Documentation:](Documentation)
  
  * [Entity Relationship Diagram Document](Documentation/ERD_Diagram_from_QuickDBD_for_Project_Gelato_Quotes_to_Scrape_DB.docx) - word doc with ERD diagram, QuickDBD input, and QuickDBD Schema output (Note: had to remove all "s
 from the QuickDBD which created problems when run in postgres.
 
  * [ETL Process Steps](Documentation/ETL_process_Steps.docx) - Notes on the ETL process in terms of loads and some work done to clean up the data. 

  * [Project Requirements](Documentation/project-requirement.md) - Requirements provided for the project. 

 
* [Resources](Resources) - 3 CSVs used for loading the tables and 1 csv for staging. 

  * [Authors Data](Resources/authors.csv) - Author data for loading 

  * [Quotes  Data](Resources/quotes.csv) - Quotes data for loading 

  * [Quote / Tag Data](Resources/quote_tags.csv) - Data exported from the quote_tags table after the ETL process to build it. 
  
  * [Staging data for Quote / Tag ETL](Resources/Mongo_raw_quote_tags.csv) - Data to be loaded in ETL-2 process (see SQL above). 


* [HTML](templates) - HTML and CSS files 

  * [HTML to Run the process](templates/index.html) - Home page for running the 6 queriesg. 

  * [CSS to Run the process](templates/style.css) - Style sheet (not implemented)  

