#!/usr/bin/python3
"""Defines a function for counting
key words in hot posts """
import requests


def count_words(subreddit, word_list, word_dict={}, after=None):
    """Gets count of key words in the titles
    of hot posts of a subreddit"""
    if len(word_dict) != len(word_list):
        word_list = [word.lower() for word in word_list]
        for word in word_list:
            word_dict[word] = 0

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    response = requests.get(
        url,
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False,
        params={"limit": 100, "after": after},
    )
    if response.status_code >= 300:
        return None
    else:
        data = response.json()
        posts = data.get("data").get("children")
        after = data.get("data").get("after")
        for post in posts:
            title = post.get("data").get("title").lower().split(" ")
            for word in word_list:
                word_dict[word] += title.count(word)

        if after is None:
            words = [[key, value] for key, value in word_dict.items()]
            words = sorted(words, key=lambda x: (-x[1], x[0]))
            for w in words:
                if w[1]:
                    print("{}: {}".format(w[0].lower(), w[1]))
            return None
        else:
            return count_words(subreddit, word_list, word_dict, after)
