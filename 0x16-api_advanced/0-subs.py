#!/usr/bin/python3
"""Script that queries subscribers on Reddit subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API."""
    # Construct the URL for the subreddit's about.json
    url = (
        f"https://www.reddit.com/r/{subreddit}/about.json"
    )

    # Headers with User-Agent
    headers = {
        "User-Agent": (
            "python:reddit_subscriber_counter:v1.0.0 "
            "(by /u/Less_Account_9562)"
        )
    }

    try:
        # Send GET request to the URL
        response = requests.get(
            url, headers=headers, allow_redirects=False
        )

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse JSON response
            data = response.json()
            # Extract number of subscribers
            subscribers = data['data']['subscribers']
            return subscribers
        elif response.status_code == 404:
            # Subreddit not found
            return 0
        else:
            # Handle other errors
            print(f"Error: {response.status_code} - {response.reason}")
            return 0

    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return 0
