#!/usr/bin/python3
"""Recursively counts keywords in the hot post titles of a subreddit."""
import requests


def ggp_print_counts(ggp_words, ggp_counts):
    """Prints the keyword counts sorted by count, then alphabetically."""
    ggp_totals = {}
    for ggp_word in ggp_counts:
        ggp_totals[ggp_word] = ggp_counts[ggp_word] * ggp_words.count(ggp_word)
    ggp_sorted = sorted(ggp_totals.items(),
                        key=lambda ggp_x: (-ggp_x[1], ggp_x[0]))
    for ggp_word, ggp_total in ggp_sorted:
        if ggp_total > 0:
            print("{}: {}".format(ggp_word, ggp_total))


def count_words(subreddit, word_list, ggp_after=None, ggp_counts=None):
    """Prints a sorted count of keywords found in the hot post titles."""
    ggp_first = ggp_counts is None
    if ggp_first:
        ggp_counts = {}
    ggp_words = [ggp_w.lower() for ggp_w in word_list]
    ggp_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    ggp_headers = {"User-Agent": "linux:api_advanced:v1.0 (by /u/ggp_user)"}
    ggp_response = requests.get(ggp_url, headers=ggp_headers,
                                params={"limit": 100, "after": ggp_after},
                                allow_redirects=False)
    if ggp_response.status_code != 200:
        if not ggp_first:
            ggp_print_counts(ggp_words, ggp_counts)
        return
    ggp_data = ggp_response.json().get("data", {})
    for ggp_post in ggp_data.get("children", []):
        ggp_title = ggp_post.get("data", {}).get("title", "")
        for ggp_word in ggp_title.lower().split():
            if ggp_word in ggp_words:
                ggp_counts[ggp_word] = ggp_counts.get(ggp_word, 0) + 1
    ggp_next = ggp_data.get("after")
    if ggp_next is None:
        ggp_print_counts(ggp_words, ggp_counts)
        return
    return count_words(subreddit, word_list, ggp_next, ggp_counts)
