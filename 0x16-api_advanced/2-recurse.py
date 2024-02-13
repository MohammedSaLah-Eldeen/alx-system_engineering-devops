#!/usr/bin/python3
"""task 2."""
import requests


def recurse(subreddit, hot_list=[]):
    """     Args:
        subreddit: subreddit name
        hot_list: list of hot titles in subreddit
        after: last hot_item appended to hot_list
    Returns:
        a list containing the titles of all hot articles for the subreddit
        or None if queried subreddit is invalid """
    global after
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requ01~ests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        next_ = response.json().get('data').get('after')
        if next_ is not None:
            after = next_
            recurse(subreddit, hot_list)
        list_titles = response.json().get('data').get('children')
        for title_ in list_titles:
            hot_list.append(title_.get('data').get('title'))
        return hot_list
    else:
        return (None)[2ests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        next_ = response.json().get('data').get('after')
        if next_ is not None:
            after = next_
     [200~def recurse(subreddit, hot_list=[]):
    """     Args:
        subreddit: subreddit name
        hot_list: list of hot titles in subreddit
        after: last hot_item appended to hot_list
    Returns:
        a list containing the titles of all hot articles for the subreddit
        or None if queried subreddit is invalid """
    global after
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requ       recurse(subreddit, hot_list)
        list_titles = response.json().get('data').get('children')
        for title_ in list_titles:
            hot_list.append(title_.get('data').get('title'))
        return hot_list
    else:
        return (None)
