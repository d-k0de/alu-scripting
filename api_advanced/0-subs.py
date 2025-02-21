#!/usr/bin/python3
"""
This module contains the function number_of_subscribers.
It queries the Reddit API to get the number of subscribers
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The subreddit name.

    Returns:
        int: Number of subscribers or 0 if subreddit is invalid.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom-User-Agent/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        except ValueError:
            return 0  # JSON decoding failed
    return 0  # Invalid subreddit or request failure
