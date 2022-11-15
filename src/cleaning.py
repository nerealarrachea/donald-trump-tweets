import pandas as pd
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import requests
from pandas import json_normalize



def cleaning_tweets(df):

    data = df.copy()
    data['original_text'] = df['text']
    data["date"] = pd.to_datetime(data["date"])
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    data['day'] = data['date'].dt.day
    
    # standard tweet preprocessing 
    data.text = data.text.str.lower()
    # Remove twitter handlers
    data.text = data.text.apply(lambda x:re.sub('@[^\s]+','',x))
    #remove hashtags
    data.text = data.text.apply(lambda x:re.sub(r'\B#\S+','',x))
    # Remove URLS
    data.text = data.text.apply(lambda x:re.sub(r"http\S+", "", x))
    # Remove all the special characters
    data.text = data.text.apply(lambda x:' '.join(re.findall(r'\w+', x)))
    # Split into Retweets and Original Content 
    data['rt_'] = data.original_text.apply(lambda x: "RT @" in x)
    # droping columns
    data.drop(["id", "date"], axis = 1, inplace = True)

    return data 

def sentiment(data):
    sid = SentimentIntensityAnalyzer()
    data.reset_index(inplace=True, drop=True)
    data[['neg', 'neu', 'pos', 'compound']] = data['text'].apply(sid.polarity_scores).apply(pd.Series)
    return data

def topic(data):
    data.loc[data.text.str.contains('mexico'), 'topic']='MEX'
    data.loc[data.text.str.contains('china'), 'topic']='CHN'
    data.loc[data.text.str.contains('fake'), 'topic']='FAKE'
    data.loc[data.text.str.contains('capitol'), 'topic']='CAP'
    data.loc[data.text.str.contains('fraud'), 'topic']='FR'
    data.loc[data.text.str.contains('border'), 'topic']='MEX'    
    data.loc[data.text.str.contains('democrat'), 'topic']='DEM'
    data.loc[data.text.str.contains('republican'), 'topic']='REP'
    data.loc[data.text.str.contains('north korea'), 'topic']='NK'
    data.loc[data.text.str.contains('russia'), 'topic']='RUS'

    
    return 

def api_():
    response = requests.get("http://127.0.0.1:9012/sql/")
    res = response.json()
    data_api = json_normalize(res)
    return data_api.head()

def api():
    params_ = { 'original_text': 'I got banned',
           'favorites': 56,
           'retweets': 67,
          'year': 2022} 
    url_ = "http://127.0.0.1:9012/insertrow"
    res = requests.post(url_, params = params_)
    return res