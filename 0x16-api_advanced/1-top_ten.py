#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts listed
for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
    - subreddit (str): The name of the subreddit (without '/r/').

    Returns:
    - None: Prints the titles of the posts or "None" if the subreddit is invalid.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'python:reddit_post_printer:v1.0.0 (by /u/Less_Account_9562)'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            
            if posts:
                for post in posts:
                    print(post.get('data', {}).get('title', ''))
            else:
                print("None")
        
        elif response.status_code == 404:
            print("None")
        
        elif response.status_code == 403:
            print("Error: 403 - Blocked")
        
        else:
            print(f"Error: {response.status_code} - {response.reason}")

    except requests.RequestException as e:
        print(f"Request failed: {e}")
