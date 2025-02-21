#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

from requests import get


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    """
    if not isinstance(subreddit, str) or not subreddit:
        print("None")
        return

    user_agent = {'User-Agent': 'python:top_ten:v1.0 (by /u/yourusername)'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 10}

    response = get(url, headers=user_agent, params=params, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    try:
        results = response.json()
        posts = results.get('data', {}).get('children', [])

        if not posts:
            print("None")
            return

        for post in posts:
            print(post.get('data', {}).get('title', "None"))

    except Exception:
        print("None")
