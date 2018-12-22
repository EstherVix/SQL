#!/usr/bin/env python2

import psycopg2


# Executes code to find the 3 most popular articles of all time in the database
def question1():
    """
    Process:
        Joins the log and articles table based on article name
        Counts the views of each article from the log table
        Orders the articles by most popular and selects top 3
    Prints:
        Statement containing the 3 most popular articles
    """
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute("""select title, count(*) as views
                    from articles, log
                    where log.path = concat('/article/', articles.slug)
                    group by title
                    order by views desc
                    limit 3;""")
    results = cursor.fetchall()
    db.close()
    print "The most popular 3 articles of all time are:"
    for row in results:
        print str(row[0]) + " -- " + str(row[1]) + " views"


# Executes code to find the most popular authors of all time in the database
def question2():
    """
    Process:
        Joins all 3 tables based on article name and author
        Counts the views of each author based on joined table
        Orders the authors by most viewed
    Prints:
    A statement containing the most viewed authors
    """
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute("""select name, count(*) as views
                    from authors, articles, log
                    where log.path = concat('/article/', articles.slug)
                    and articles.author = authors.id
                    group by name
                    order by views desc;""")
    results = cursor.fetchall()
    db.close()
    print "The most popular article authours of all time are:"
    for row in results:
        print str(row[0]) + " -- " + str(row[1]) + " views"


# Executes code to find days where more than 1% of requests lead to errors
def question3():
    """
    Process:
        Subquery 1 (Total) - Selects a table showing total queries for each day
        Subquery 2 (Fail) - Selects a table showing total errors for each day
        Joins Subquery 1 and Subquery 2 by data
        Calculates percentage error by dividing total errors by total queries
        Filters out dates where errors are less than 1%
        Orders results by highest percentage error for that date
    Return:
    A statement with days where 1%+ of requests lead to errors
    """
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute("""select day, (fail * 100.0 / total)
                    as percent_errors
                    from (select cast(time as date)as day,
                            count(status) as total
                            from log
                            group by day) as total,
                    (select cast(time as date) as date,
                            count(*)as fail from log
                            where status != '200 OK'
                            group by date)  as fail
                    where fail.date = total.day
                    and (fail * 100.0 / total) > 1.0
                    order by percent_errors desc;
                    """)
    results = cursor.fetchall()
    db.close()
    print """Days where more than 1% of requests lead to errors are:"""
    for row in results:
        print str(row[0]) + " -- " + str('%.2f' % row[1]) + "% errors"


# Executes function that prints out all the results
def database_analysis():
    print question1()
    print " "
    print question2()
    print " "
    print question3()
    print " "


if __name__ == '__main__':
    database_analysis()
