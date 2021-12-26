import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
import emoji

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

def extract_emojis(df):
    emojis_dict = {}
    for text in df['tweet_content']:
        for i in text:
            if i in emoji.UNICODE_EMOJI['en']:
                emojis_dict[i] = 0

    for i in emojis_dict:
        for text in df['tweet_content']:
            emojis_dict[i] += text.count(i)

    sorted_tuple = sorted(emojis_dict.items(), key=lambda x: x[1], reverse=True)
    emojis_dict = dict(sorted_tuple)
    print(pd.DataFrame(list(emojis_dict.items()),
                       columns=['emoji', 'amount']))

def frequent_words(df):
    freq = []
    for tweet in df['tweet_content']:
        lemmatizer = WordNetLemmatizer()
        word_list = nltk.word_tokenize(tweet)
        lemmatized_output = [lemmatizer.lemmatize(w) for w in word_list]
        if 'pos' in df.name:
            for i in lemmatized_output:
                i.lower()
                if i in pos:
                    freq.append(i)
        else:
            for i in lemmatized_output:
                i.lower()
                if i in neg:
                    freq.append(i)
    freq_dict = {}
    for word in freq:
        freq_dict[word] = freq.count(word)
    sorted_tuple = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    freq_dict = dict(sorted_tuple)
    print(list(freq_dict.keys())[:10])

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

new = new_data_df['tweet_content'].apply(sentiment)
new_data_df = new_data_df.assign(sentiment_score=new)
new_data_df = new_data_df.sort_values(by='sentiment_score')
pos_tweets_df = new_data_df.loc[new_data_df['sentiment_score'] >= new_data_df['sentiment_score'].quantile(q=[0.9])[0.9]]
pos_tweets_df.name = 'pos_tweets_df'
neg_tweets_df = new_data_df.loc[new_data_df['sentiment_score'] <= new_data_df['sentiment_score'].quantile(q=[0.1])[0.1]]
neg_tweets_df.name = 'neg_tweets_df'

frequent_words(neg_tweets_df)
frequent_words(pos_tweets_df)
extract_emojis(new_data_df)