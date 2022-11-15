# Visualization
import plotly.express as px
import seaborn as sns
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud,STOPWORDS
from PIL import Image
import numpy as np



def pie_(data):
    pos_neg = (data['compound']>0).sum() + (data['compound']<0).sum()
    total = data.shape[0]
    neutral = total - pos_neg
    # Pie chart
    labels = ['Positive', 'Negative', 'Neutral']
    sizes = [(data['compound']>0).sum(), (data['compound']<0).sum(), neutral]
    #colors
    colors = ['#99ff99','#ff9999','#66b3ff']
    #explsion
    explode = (0.05,0.05,0.05)
    plt.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode = explode)
    #draw circle
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.title("What's Donald Trump's mood?")
    plt.tight_layout()
    return plt.show()

def over_the_years(data):
    
    counts = pd.DataFrame(data['year'].value_counts()).reset_index()
    counts.columns = ['year', 'count']
    
    fig = go.Figure(go.Bar(
    name="Annual Count", 
    x=counts.year, 
    y=counts['count'], 
    marker_color=counts['count'] 
    ))
    fig.update_layout(template='ggplot2', title="Tweets over the years")
    return fig.show()

def scatter(df,title):
    fig = px.scatter(df, x = df['compound'], y = df['retweets'], color = df['topic'], hover_name = df['original_text'], height=500, width=1000, title=title)
    fig.write_html("images/save.html")
    return fig.show()

def _scatter(df,title):
    fig = px.scatter(df, x = df['compound'], y = df['retweets'], color = df['topic'], hover_name = df['original_text'], height=500, width=1000, title=title)
    fig.write_html("images/extra.html")
    return fig.show()

def scatter__(df,title):
    fig = px.scatter(df, x = df['compound'], y = df['retweets'], color = df['topic'], hover_name = df['original_text'], height=500, width=1000, title=title)
    fig.write_html("images/countries.html")
    return fig.show()

def scatter_(df,title):
    fig = px.scatter(df, x = df['compound'], y = df['retweets'], hover_name = df['original_text'], height=500, width=1000, title=title)
    fig.write_html(f"images/gen.html")
    return fig.show()

def word_cloud(data, rep_word):
    maskArray = np.array(Image.open("images/perfil.png"))
    words = ' '.join(data)
    STOPWORDS.update(["https", "co","rt","the", "a", "an", "in","s", "amp","u", rep_word])    
    cleaned_word = " ".join([word for word in words.split()])
    wordcloud = WordCloud(stopwords = STOPWORDS,
                         background_color = 'white',
                          min_font_size = 5,
                         max_words=50,
                          mask = maskArray,
                          contour_color='black',contour_width=3
                         ).generate(cleaned_word)
    plt.figure(figsize = (10,10), facecolor=None)
    plt.imshow(wordcloud,interpolation='bilinear')
    plt.tight_layout(pad = 0)
    plt.axis('off')
    return plt.show()