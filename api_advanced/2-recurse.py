#!/usr/bin/python3
"""Recursively queries the Reddit API for all hot posts of a subreddit."""
import requests


def recurse(subreddit, hot_list=None, ggp_after=None):
    """Returns a list of the titles of all hot posts, None if invalid."""
    if hot_list is None:
        hot_list = []
    ggp_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    ggp_headers = {"User-Agent": "linux:api_advanced:v1.0 (by /u/ggp_user)"}
    ggp_response = requests.get(ggp_url, headers=ggp_headers,
                                params={"limit": 100, "after": ggp_after},
                                allow_redirects=False)
    if ggp_response.status_code != 200:
        return hot_list if hot_list else None
    ggp_data = ggp_response.json().get("data", {})
    hot_list.extend([ggp_post.get("data", {}).get("title")
                     for ggp_post in ggp_data.get("children", [])])
    ggp_next = ggp_data.get("after")
    if ggp_next is None:
        return hot_list if hot_list else None
    return recurse(subreddit, hot_list, ggp_next)
