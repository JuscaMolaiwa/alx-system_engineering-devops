#!/usr/bin/python3
"""Queries the Reddit API."""

import requests


def top_ten(subreddit):
    """Queries the Reddit API."""
    try:
        response = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "python:top_ten_script:v1.0.0 (by /u/JuicesKemishi)"},
                            allow_redirects=False)

        # Check for successful request
        if response.status_code == 200:
            # Ensure the response content type is JSON
            if response.headers.get('Content-Type') == 'application/json':
                data = response.json()
                posts = data.get('data', {}).get('children', [])

                if posts:
                    for post in posts:
                        print(post.get('data', {}).get('title', ''))
                else:
                    print("None")
            else:
                print("Invalid response format")
        elif response.status_code == 404:
            print("None")

        elif response.status_code == 403:
            print("Error: 403 - Blocked.")
        else:
            print(f"Error: {response.status_code} - {response.reason}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
