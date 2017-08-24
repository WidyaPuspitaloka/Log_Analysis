#!/usr/bin/env python3
######################################################
# Project 3: Log Analysis
# Date Created: 08/24/2017
# Submitted by: Widya Puspitaloka
# Description: This file creates reporting tool using
#              the psycopg2 module to connect to
#              the database that prints out reports
#              based on the data in the database
######################################################

import psycopg2

# 1. What are the most popular three articles of all time?
query_1_title = "What are the most popular three articles of all time?"
query_1 = """
    select articles.title, count (*) as views
    from articles
    join log on log.path = concat('/article/',articles.slug)
    group by articles.title order by views desc limit 3
    """

# 2. Who are the most popular article authors of all time?
query_2_title = "Who are the most popular article authors of all time?"
query_2 = """
    select authors.name, count (*) as views
    from articles
    join authors on articles.author = authors.id
    join log on log.path = concat('/article/',articles.slug)
    group by authors.name order by views desc
    """

# 3. On which days did more than 1% of requests lead to errors?
query_3_title = "On which days did more than 1% of requests lead to errors?"
query_3 = """
    select *
    from (select date(time),round(100.0 * sum(case log.status
    when '404 NOT FOUND' then 1 else 0 end)/count(log.status),2)
    as error from log
    group by date(time) order by error desc)
    as subq where error > 1;
    """


def connect(dbname="news"):
    """Connect to the PostgreSQL database and return a database connection"""
    try:
        db = psycopg2.connect("dbname={}".format(dbname))
        c = db.cursor()
        return db, c
    except:
        print ("Unable to connect to the database")


def popular_articles(query_1):
    """Return & print the three most popular articles results"""
    db, c = connect()
    c.execute(query_1)
    db.commit()
    result = c.fetchall()
    for i in range(len(result)):
        print ('\t', i + 1, '-', result[i][0], '\t --', result[i][1], 'views')
    db.close()


def popular_authors(query_2):
    """Return & print most popular authors results"""
    db, c = connect()
    c.execute(query_2)
    db.commit()
    result = c.fetchall()
    for i in range(len(result)):
        print ('\t', i + 1, '-', result[i][0], '\t --', result[i][1], 'views')
    db.close()


def error_status(query_3):
    """Return & print the day that more than 1% of requests lead to errors"""
    db, c = connect()
    c.execute(query_3)
    db.commit()
    result = c.fetchall()
    for i in range(len(result)):
        print ('\t', result[i][0], '\t --', result[i][1], '% errors')
    db.close()

if __name__ == '__main__':
    print ("Result")
    print("The List of The Most Popular Three Articles:")
    popular_articles(query_1)
    print("The List of Most Popular Article Authors of All Time:")
    popular_authors(query_2)
    print("The Day on Which More Than 1% of Requests Lead to Errors:")
    error_status(query_3)
