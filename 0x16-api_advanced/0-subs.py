#!/usr/bin/python3
""" This script will query the Reddit API and return number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ request number of subscribers of a subredit"""
    url = f"https://www.reddit.com/r/{subreddit}/about/.json"
    headers = {'User-Agent': 'my-app/0.0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            all_r = response.json()
            data = all_r.get('data')
            sub_count = data.get('subscribers')
            return sub_count
        else:
            return 0
    except requests.RequestException:
        return 0
