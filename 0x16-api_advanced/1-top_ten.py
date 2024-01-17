#!/usr/bin/python3
"""Defines a function for retrieving
hot posts of subreddit"""
import requests


def top_ten(subreddit):
    """
    Gets the top 10 posts of
    a subreddit.

    Args:
        subreddit (str): the name of the subreddit

    Returns:
        Prints list to stdout else None
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    response = requests.get(
        url, headers={"User-Agent": "My-User-Agent"}, allow_redirects=False
    )
    if response.status_code >= 300:
        print("None")
    else:
        data = response.json()
        posts = data.get("data").get("children")
        for post in posts:
            print(post.get("data").get("title"))
