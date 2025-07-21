#!/usr/bin/env python3

import requests 
import argparse

def register_user(username,email,role,cli=False):
    """ register new user via API"""
    if cli:
        # create parser
        parser = argparse.ArgumentParser(description="pass user details")
        parser.add_argument("username", help="Give the email of user")
        parser.add_argument("email")
        parser.add_argument("role")
        args = parser.parse_args()
        print (args.username,args.email,args.role)
        payload = {username:args.username,
                    email:args.email,
                    role:args.role}
    else:
        payload = {username:f"{username}",
                    email:f"{email}",
                    role:f"{role}"}
    try:
        r = requests.post(url='https://httpbin.org/post',data=payload) # set Content-Type: application/json header and serializes the payload to JSON
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print("HTTP err:", err)
    except requests.exceptions.RequestException as err:
        # for timeouts or connection errors
        print("Connection or timeout issue:",err)

    print("Response:", r.json())


if __name__ == "__main__":

    register_user("alex","alex@dejanu","SRE",cli=True)

