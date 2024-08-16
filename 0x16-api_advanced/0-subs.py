#!/usr/bin/python3
"""Script that queries subscribers on Reddit subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a subreddit."""

    url = f"https://oauth.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        data = response.json()
        return data['data']['subscribers']
    except requests.exceptions.RequestException:
        return 0
