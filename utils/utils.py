import os
import sys

import feedparser
import httpx
import tweepy
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

"""
Twitter Authentification Credentials
Please update with your own credentials
"""
cons_key = os.getenv("cons_key")
cons_secret = os.getenv("cons_secret")
acc_token = os.getenv("acc_token")
acc_secret = os.getenv("acc_secret")


def get_twitter_auth():
    """
    @return:
        - the authentification to Twitter
    """
    try:
        consumer_key = cons_key
        consumer_secret = cons_secret
        access_token = acc_token
        access_secret = acc_secret

    except KeyError:
        sys.stderr.write("Twitter Environment Variable not Set\n")
        sys.exit(1)

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    return auth


def get_twitter_client():
    """
    @return:
        - the client to access the authentification API
    """
    auth = get_twitter_auth()
    client = tweepy.API(auth, wait_on_rate_limit=True)
    return client


def get_feed(url) -> list:
    urls = (
        url,
    )

    # get the RSS feeds from feedparser
    feeds = [feedparser.parse(url) for url in urls]
    all_entries = [feed.entries for feed in feeds]

    return all_entries


def get_soup(url):
    re = httpx.get(url, headers=headers)
    soup = BeautifulSoup(re.content, 'lxml')
    if re.status_code == 404:
        return None
    else:
        return soup


def get_status(url):
    re = httpx.get(url, headers=headers)
    if re.status_code != 200:
        raise Exception("API response: {}".format(re.status_code))
    else:
        return re.status_code
