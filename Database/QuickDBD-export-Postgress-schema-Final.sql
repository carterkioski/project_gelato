-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Schema for Project 2 - ETL - project gelato
-- Revised to correct spelling of description, make the quote_id serial
-- Postgres Database: Quotes_to_Scrape_DB
-- Create tables that other tables are dependent on first to avoid foreign key creation issues

CREATE TABLE Author (
    author_name 	varchar(50)   	NOT NULL,
    born 		varchar(40)   	NOT NULL,
    description 	text   		NOT NULL,
    CONSTRAINT pk_Author PRIMARY KEY (author_name)
);

CREATE TABLE Quotes (
    quote_id 		serial   	NOT NULL,
    author_name 	varchar(50)   	NOT NULL,
    text 		text   		NOT NULL,
    CONSTRAINT pk_Quotes PRIMARY KEY (quote_id)
);

CREATE TABLE Quote_tags (
    quote_id 		int   		NOT NULL,
    tag 		text   		NOT NULL,
    CONSTRAINT pk_Quote_tags PRIMARY KEY (quote_id,tag)
);

ALTER TABLE Quotes ADD CONSTRAINT fk_Quotes_author_name FOREIGN KEY(author_name)
REFERENCES Author (author_name);

ALTER TABLE Quote_tags ADD CONSTRAINT fk_Quote_tags_quote_id FOREIGN KEY(quote_id)
REFERENCES Quotes (quote_id);
