import json
import datetime
import pandas as pd
from collections import Counter


def flatten_tweets(tweets, tweet_columns, keywords):
    """ Flattens out tweet dictionaries so relevant JSON is
        in a top-level dictionary. """

    tweets_list = []

    # Iterate through each tweet
    for tweet_obj in tweets:
        tweet_info = {
            column_name: None for column_name in tweet_columns
        }
        tweet_info['keywords'] = {}
        #date
        date = datetime.datetime.strptime(tweet_obj['created_at'], '%a %b %d %H:%M:%S %z %Y')
        tweet_info['date'] = date

        #followers
        followers = tweet_obj['user']['followers_count']
        tweet_info['followers'] = followers

        #retweets
        retweets = tweet_obj['retweet_count']
        tweet_info['retweets'] = retweets

        #favorited
        favorite_count = tweet_obj['favorite_count']
        tweet_info['favorite_count'] = favorite_count

        #keywords
        fulltext = tweet_obj['text']
        print(fulltext)
        for word in keywords:
            word_matches = fulltext.count(word)
            tweet_info['keywords'].update({word: word_matches})

        tweets_list.append(tweet_info)

    return tweets_list


def select_text(tweets):
    ''' Assigns the main text to only one column depending
        on whether the tweet is a RT/quote or not'''

    tweets_list = []

    # Iterate through each tweet
    for tweet_obj in tweets:

        if 'retweeted_status-extended_tweet-full_text' in tweet_obj:
            tweet_obj['text'] = \
                tweet_obj['retweeted_status-extended_tweet-full_text']

        elif 'retweeted_status-text' in tweet_obj:
            tweet_obj['text'] = tweet_obj['retweeted_status-text']

        elif 'extended_tweet-full_text' in tweet_obj:
            tweet_obj['text'] = tweet_obj['extended_tweet-full_text']

        tweets_list.append(tweet_obj)

    return tweets_list

if __name__ == '__main__':
    with open('twitter.json', 'r') as json_input_file:
        json_contents = json.load(json_input_file)

    keywords = ['genetic']
    columns = ['biotech_word', 'tweets_containing', 'retweet_count', 'date', 'followers', 'favorited']
    tweet_columns = ['list_of_relevant_words', 'followers', 'retweets', 'date', 'favorite_count']
    output = {

    }

    tweets = flatten_tweets(json_contents['statuses'], tweet_columns, keywords)

    counts = Counter({'tweets_containing': 0, 'retweet_count': 0, 'favorite_count': 0})
    word_rows = {k: counts for k in keywords}

    for tweet in tweets:
        for keyword in keywords:
            word_rows[keyword].update({'retweet_count': tweet['retweets']})

            if keyword in tweet['keywords'] and tweet['keywords'][keyword] > 0:
                word_rows[keyword].update({'tweets_containing': 1})
            word_rows[keyword].update({'favorite_count': tweet['favorite_count']})


    df = pd.DataFrame([dict({'word':k}, **word_rows[k]) for k in word_rows])
    print(word_rows)

