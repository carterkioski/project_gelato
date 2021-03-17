-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Schema for Project 2 - Projct gelato - Database: Quotes_to_Scrape_DB
-- Create tables that other tables are dependent on first to avoid foreign key creation in dependent tables

CREATE TABLE "Quotes" (
    "quote_id" varchar(5)   NOT NULL,
    "author_name" varchar(50)   NOT NULL,
    "text" varchar(100)   NOT NULL,
    CONSTRAINT "pk_Quotes" PRIMARY KEY (
        "quote_id"
     )
);

CREATE TABLE "Author" (
    "author_name" varchar(50)   NOT NULL,
    "born" varchar(40)   NOT NULL,
    "desription" text   NOT NULL,
    CONSTRAINT "pk_Author" PRIMARY KEY (
        "author_name"
     )
);

-- Need to check the limit on text, and storage efficiency
CREATE TABLE "Quote_Tags" (
    "quote_id" varchar(5)   NOT NULL,
    "tag" varchar(20)   NOT NULL,
    CONSTRAINT "pk_Quote_Tags" PRIMARY KEY (
        "quote_id","tag"
     )
);

ALTER TABLE "Quotes" ADD CONSTRAINT "fk_Quotes_author_name" FOREIGN KEY("author_name")
REFERENCES "Author" ("author_name");

ALTER TABLE "Quote_Tags" ADD CONSTRAINT "fk_Quote_Tags_quote_id" FOREIGN KEY("quote_id")
REFERENCES "Quotes" ("quote_id");

