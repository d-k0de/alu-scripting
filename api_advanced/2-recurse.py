#!/usr/bin/python3
"""Recursively fetches hot article titles from a subreddit."""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of hot post titles or None if invalid."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, params={'after': after})

    if res.status_code != 200:
        return None

    data = res.json().get('data', {})
    hot_list.extend(post['data']['title'] for post in data.get('children', []))

    return recurse(subreddit, hot_list, after=data.get('after')) if data.get('after') else hot_list
