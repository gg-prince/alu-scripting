#!/usr/bin/python3
"""Queries the Reddit API for the subscribers of a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers of a subreddit, 0 if invalid."""
    ggp_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    ggp_headers = {"User-Agent": "linux:api_advanced:v1.0 (by /u/ggp_user)"}
    ggp_response = requests.get(ggp_url, headers=ggp_headers,
                                allow_redirects=False)
    if ggp_response.status_code != 200:
        return 0
    return ggp_response.json().get("data", {}).get("subscribers", 0)
