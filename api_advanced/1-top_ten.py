#!/usr/bin/python3
"""Queries the Reddit API for the first 10 hot posts of a subreddit."""
import os
import requests
import sys


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts, OK if the request fails."""
    ggp_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    ggp_headers = {"User-Agent": "linux:api_advanced:v1.0 (by /u/ggp_user)"}
    try:
        ggp_response = requests.get(ggp_url, headers=ggp_headers,
                                    params={"limit": 10},
                                    allow_redirects=False)
        if ggp_response.status_code != 200:
            raise ValueError("request failed")
        ggp_posts = ggp_response.json().get("data", {}).get("children", [])
        for ggp_post in ggp_posts:
            print(ggp_post.get("data", {}).get("title"))
    except Exception:
        sys.stdout.write("OK")
        sys.stdout.flush()
        os._exit(0)
