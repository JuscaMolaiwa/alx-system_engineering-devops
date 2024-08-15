#!/usr/bin/python3
"""Script to query hot articles on Reddit."""
import requests


def count_words(subreddit, word_list, after="", word_count=None):
    """Recursively retrieves hot post titles from a given subreddit."""
    # Initialize word_count if it's None
    if word_count is None:
        word_count = {}
    # Normalize all words in word_list to lowercase
    word_list = [word.lower() for word in word_list]
    # Construct the URL for the subreddit's hot posts in JSON format
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    # Define headers for the HTTP request
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    # Define parameters for the request, including pagination and limit
    params = {
        "after": after,
        "limit": 100
    }
    # Send a GET request to the subreddit's hot posts page
    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        # Check if the response status code indicates a not-found error (404)
        if response.status_code == 404:
            return
        # Ensure the content type is JSON
        if "application/json" not in response.headers.get("Content-Type", ""):
            return
        # Parse the JSON response and extract relevant data
        data = response.json().get("data", {})
        after = data.get("after")
        # Get the titles of all hot posts
        titles = [
            child.get("data", {}).get("title", "").lower()
            for child in data.get("children", [])
        ]
        # Count the occurrences of each keyword in the titles
        for title in titles:
            # Split the title into words, ignoring punctuation
            words_in_title = title.split()
            # Count occurrences of each word in word_list
            for word in word_list:
                count = words_in_title.count(word)
                word_count[word] = word_count.get(word, 0) + count
        # Recursively call the function if there are more posts to retrieve
        if after:
            return count_words(subreddit, word_list, after, word_count)
        # Sort the word_count dictionary by count (descending)
        # and then alphabetically by word (ascending)
        sorted_word_count = sorted(
            word_count.items(),
            key=lambda kv: (-kv[1], kv[0])
        )
        # Print the sorted word counts, skipping words with a count of 0
        for word, count in sorted_word_count:
            if count > 0:
                print(f"{word}: {count}")
    except requests.exceptions.RequestException:
        return
