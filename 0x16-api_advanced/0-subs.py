#!/usr/bin/python3
"""task 0."""
import requests


def number_of_subscribers(subreddit):
    """solution for task 0"""
    headers = {'User-Agent': 'MyCoolScript/1.0 (by /u/supermaker)'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    else:
        return (0)


