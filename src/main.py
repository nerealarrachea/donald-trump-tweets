from flask import Flask, request, jsonify
import random
import numpy as np
import markdown.extensions.fenced_code
import sql_queries as esecuele
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


app = Flask(__name__)

# Render the markdwon
@app.route("/")
def readme ():
    readme_file = open("README.md", "r")
    return markdown.markdown(readme_file.read(), extensions = ["fenced_code"])

# GET ENDPOINTS: SQL 
# SQL get everything
@app.route("/sql/")
def sql ():
    return jsonify(esecuele.get_everything())

# SQL get positive
@app.route("/pos/")
def pos ():
    return jsonify(esecuele.get_positive())

# SQL get negative
@app.route("/neg/")
def neg ():
    return jsonify(esecuele.get_negative())

# SQL get favs
@app.route("/fav/")
def fav ():
    return jsonify(esecuele.get_favs())

# SQL get retweets
@app.route("/retweets/")
def retweets ():
    return jsonify(esecuele.get_retweets())

# SQL get year
@app.route("/year/<year>")
def year (year):
    return jsonify(esecuele.get_year(year))

####### POST
@app.route("/insertrow", methods=["POST"])
def try_post ():
    # Decoding params
    my_params = request.args
    original_text = my_params["original_text"]
    favorites = my_params["favorites"]
    retweets = my_params["retweets"]
    year = my_params["year"]

    # Passing to my function: do the insert
    esecuele.insert_one_row(original_text, favorites, retweets, year)
    return f"Query succesfully inserted"


if __name__ == "__main__":
    app.run(port=9012, debug=True)