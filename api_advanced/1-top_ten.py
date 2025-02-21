#!/usr/bin/python3
"""Get the titles of the first 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):

    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")  # Ensure "None" is printed properly
        return

    posts = response.json().get('data', {}).get('children', [])
    
    if not posts:  # If subreddit exists but has no posts
        print("None")
        return

    for i in range(min(10, len(posts))):
        print(posts[i].get('data', {}).get('title'))
