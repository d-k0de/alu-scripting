#!/usr/bin/python3
"""Get the titles of the first 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):

    """Print titles of top 10 hot posts for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {}).get('children', [])
            for i in range(min(10, len(data))):
                title = data[i].get('data', {}).get('title')
                if title:
                    print(title)
            print("OK")
        else:
            print(None)
    except:
        print(None)
