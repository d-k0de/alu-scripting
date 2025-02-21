#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom-User-Agent/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if request was successful and response is JSON
    if response.status_code == 200:
        try:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        except ValueError:
            return 0  # JSON decoding failed
    else:
        return 0  # Invalid subreddit or request failure

