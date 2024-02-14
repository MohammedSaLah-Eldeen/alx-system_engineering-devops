#!/usr/bin/python3
"""task 0."""
import requests


def number_of_subscribers(subreddit):
    """solution for task 1"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return (0)
    return (response.json().get("data").get("subscribers"))
