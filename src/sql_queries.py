from sql_connection import engine
import pandas as pd

def get_everything ():
    query = """SELECT * FROM trump_tweets;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


def get_positive ():
    query = """SELECT original_text FROM trump_tweets
    WHERE compound > 0.0;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


def get_negative ():
    query = """SELECT original_text FROM trump_tweets
    WHERE compound < 0.0;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


def get_favs ():
    query = """SELECT original_text, favorites FROM trump_tweets
    ORDER BY favorites DESC;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


def get_retweets ():
    query = """SELECT original_text, retweets FROM trump_tweets
    ORDER BY retweets DESC;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


def get_year (year):
    query = f"""SELECT original_text FROM trump_tweets
    WHERE year = {year}
    ORDER BY favorites DESC;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


def insert_one_row (original_text, favorites, retweets, year):
    query = f"""INSERT INTO trump_tweets
     (original_text, favorites, retweets, year) 
        VALUES ('{original_text}', {favorites}, {retweets}, '{year}');
    """
    engine.execute(query)
    return f"Correctly introduced!"