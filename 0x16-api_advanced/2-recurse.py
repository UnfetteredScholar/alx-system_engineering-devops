#!/usr/bin/python3
"""Defines a function for listing
all hot posts"""
import requests


def recurse(subreddit, hot_list=[], count=None, after=None):
    """Gets all hot posts of a subreddit"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    response = requests.get(
        url,
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False,
        params={"count": count, "after": after},
    )
    if response.status_code >= 400:
        return None
    else:
        data = response.json()
        posts = data.get("data").get("children")
        after = data.get("data").get("after")
        count = data.get("data").get("count")
        for post in posts:
            hot_list.append(post.get("data").get("title"))

        if not after:
            return hot_list
        else:
            return recurse(subreddit, hot_list, count, after)
