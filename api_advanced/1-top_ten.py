#!/usr/bin/python3
"""
1-top_ten
"""
import requests

def top_ten(subreddit):
    """If not a valid subreddit, print None"""
    headers = {'User-Agent': 'python:top_ten:v1.0 (by /u/your_username)'}
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        print(None)
        return
        
    results = response.json().get('data', {}).get('children', [])
    
    if not results:
        print(None)
        return
        
    for post in results:
        print(post.get('data', {}).get('title'))
