#!/usr/bin/python3
"""This script  queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a subreddit."""
import requests


def top_ten(subreddit):
    """ request print top 10 post for a given subredit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agents': 'api/advanced, task1'}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        results = data.get("data")
        [print(c.get("data").get("title")) for c in results.get("children")]
    else:
        print("None")
