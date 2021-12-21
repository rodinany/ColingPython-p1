import pandas as pd
import nltk
#nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
import numpy as np

data_df = pd.read_csv('tweets.csv')
new_data_df = data_df.dropna()
author_names = set(new_data_df['author_name'])

for author in author_names:
    tweet_info = pd.DataFrame()
    if len(author.split()) >= 2:
        tweets = new_data_df.loc[new_data_df['author_name'] == author]
        tweet_info = tweet_info.append(tweets, ignore_index=True)
        for i in tweet_info["tweet_content"].values:
            if len(i) == min(map(len, tweet_info["tweet_content"].values)):
                #print(f'{author} {i}')

neg = set()
with open('negative-words.txt', 'r', encoding='cp1250') as f:
    for line in f:
        if line[0] != ';':
            neg.add(line.strip('\n'))

pos = set()
with open('positive-words.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        if line[0] != ';':
            pos.add(line.strip('\n'))

def sentiment(tweet):
    n = 0
    lemmatizer = WordNetLemmatizer()
    word_list = nltk.word_tokenize(tweet)
    lemmatized_output = [lemmatizer.lemmatize(w) for w in word_list]
    for i in lemmatized_output:
        i.lower()
        if i in neg:
            n -= 1
        elif i in pos:
            n += 1
    return n

new = new_data_df['tweet_content'].apply(sentiment)
new_data_df['sentiment_score'] = new
