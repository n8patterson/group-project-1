import json
import re
import requests
import os

TWITTER_TOKEN = os.environ.get('TWITTER_TOKEN')

handle_pattern = re.compile(r'@[A-Za-z_]+')


twitter_headers = {"Authorization": "Bearer {bearer_token}".format(bearer_token=TWITTER_TOKEN)}
twitter_get_user_id_url = 'https://api.twitter.com/2/users/by/username/{username}'
twitter_get_tweets_for_user = 'https://api.twitter.com/2/users/{user_id}/tweets?tweet.fields=created_at&max_results=100'

with open('biotech_influcencers.txt', 'r') as _file:
    contents = _file.read()

handles = re.findall(handle_pattern, contents)


def get_id_by_handle(username):
    endpoint = twitter_get_user_id_url.format(username=username[1:])
    response = json.loads(requests.get(endpoint, headers=twitter_headers).text)
    return response['data']['id']


def get_tweets_batch(user_name, user_id):
    print(f'getting tweets from {user_name}...')
    next_page = None
    has_next = True
    counter = 0
    while has_next:
        counter +=1
        endpoint = twitter_get_tweets_for_user.format(user_id=user_id)
        if next_page is not None:
            endpoint = f'{endpoint}&pagination_token={next_page}'
        try:
            print(f"fetching page {counter}...")
            response = json.loads(requests.get(endpoint, headers=twitter_headers).text)
            tweets = response['data']
            next_page = response['meta'].get('next_token', None)
            print("success")
        except Exception as e:
            has_next, next_page = None, None
            print(f"failed: {e}")
            continue
        has_next = True if next_page else False

        yield tweets


account_ids = {h: get_id_by_handle(h) for h in handles}
tweets = {username: [] for username, account in account_ids.items()}

print(account_ids)
for username, account_id in account_ids.items():
    for tweet_batch in get_tweets_batch(username, account_id):
        tweets[username].extend(tweet_batch)


with open('influencer_tweets.json', 'w', encoding='utf-8') as f:
    json.dump(tweets, f, ensure_ascii=False, indent=4)



