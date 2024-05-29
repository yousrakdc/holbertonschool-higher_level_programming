#!/usr/bin/env python3
"""
Script to consume and process data from an API using Python.

This script performs the following tasks:
1. Fetches posts from a JSONPlaceholder API and prints the titles.
2. Fetches posts from the API and saves them to a CSV file.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch posts from the API and print their titles.

    This function sends a GET request to the JSONPlaceholder API to retrieve
    posts. If the request is successful (status code 200), it parses the JSON
    response and prints the title of each post.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetch posts from the API and save them to a CSV file.

    This function sends a GET request to the JSONPlaceholder API to retrieve
    posts. If the request is successful (status code 200), it parses the JSON
    response, extracts relevant fields from each post, and writes them to a
    CSV file named 'posts.csv'.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()
        posts_data = [{
            'id': post['id'],
            'title': post['title'],
            'body': post['body']
        } for post in posts]

        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts_data)
