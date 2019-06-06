from getpass import getpass
import requests
from requests.exceptions import HTTPError
from requests.auth import HTTPDigestAuth
import json
import os


def basic_request (url='https://api.github.com'):
    """basic request no auth"""
    try:
        response =  requests.get('https://api.github.com')
    #response.status_code == 200:
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
        #return message body content as  bytes
        return response.content

def request_pass_auth(url="https://api.github.com/repos/dejanu/linux/commits"):
    """request with user and pass as environ vars"""
    u = os.environ["u"]
    p = os.environ["pas"]
    r = requests.get("https://api.github.com/repos/dejanu/linux/commits",params={'per_page': '100'}, verify=False,auth=HTTPDigestAuth(u,p))
    if r.status_code == 200:
        # get the content as  a list
        parsed = json.loads(r.content)
        return parsed


if __name__ == "__main__":

    print(basic_request)
