#!/usr/bin/python3
"""Defines a function for retrieving
number of subreddit subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
    Gets the number of subscribers to
    a subreddit.

    Args:
        subreddit (str): the name of the subreddit

    Returns:
        The number of subs else 0 for invalid name.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(
            url, headers={"User-Agent": "My-User-Agent"}, allow_redirects=False
        )
        data = response.json()
        return data["data"]["subscribers"]
    except Exception as ex:
        return 0
