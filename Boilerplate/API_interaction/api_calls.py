#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import os

def get_github_users_by_location(location, token=None):
    """" pagination returns 30 items per page, so if there are more than 30 users in the location,
    the response will have a key called "next" which will have the link to the next page.
    """
    url = "https://api.github.com/search/users"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "Authorization": f"token {token}"
    }

    params = {
        "q": f"location:{location}"
    }
    
    response = requests.get(url, headers=headers, params=params)
        
    data = response.json()
    print(f"Number of users found in {location}: ", data["total_count"])
    # print("No of users returned: ", len(data["items"])) 
    # return data

if __name__ == "__main__":

    location_list = ['Austria', 'Belgium', 'Bulgaria', 'Denmark', 'France', 'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Romania', 'Switzerland']

    # check if token is set as env variable
    try:
        token = os.environ["GITHUB_TOKEN"]
    except KeyError:
        print("Please set the environment variable GITHUB_TOKEN")
        exit(1)

    for location in location_list:
        users = get_github_users_by_location(location, token=token)
