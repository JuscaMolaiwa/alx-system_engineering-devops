#!/usr/bin/python3
"""
Script to query a list of all hot posts on a given Reddit subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively retrieves a list of titles of all hot posts
    on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): List to store the post titles.
                                    Default is an empty list.
        after (str, optional): Token used for pagination.
                                Default is an empty string.
        count (int, optional): Current count of retrieved posts. Default is 0.

    Returns:
        list: A list of post titles from the hot section of the subreddit,
              or None if the subreddit is invalid.
    """
    # Construct the URL for the subreddit's hot posts in JSON format
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Define parameters for the request, including pagination and limit
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    try:
        # Send a GET request to the subreddit's hot posts page
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        # Check if the response status code is 404 (not found)
        if response.status_code == 404:
            return None

        # Ensure the content type is JSON
        if "application/json" not in response.headers.get("Content-Type", ""):
            return None

        # Parse the JSON response and extract relevant data
        data = response.json().get("data")
        if data is None:
            return None

        # Update the pagination token and post count
        after = data.get("after")
        count += data.get("dist", 0)

        # Append post titles to the hot_list
        for child in data.get("children", []):
            hot_list.append(child.get("data", {}).get("title"))

        # Recursively call the function if there are more posts to retrieve
        if after:
            return recurse(subreddit, hot_list, after, count)

        # Return the final list of hot post titles
        return hot_list

    except requests.exceptions.RequestException as e:
        # Handle any requests-related errors (e.g., network issues)
        print(f"Request error: {e}")
        return None

    except ValueError as e:
        # Handle errors in JSON decoding
        print(f"JSON decoding error: {e}")
        return None
