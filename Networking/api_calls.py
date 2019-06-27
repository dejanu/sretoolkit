from getpass import getpass
import requests
from requests.exceptions import HTTPError
from requests.auth import HTTPDigestAuth
import json
import os

#HTTP headers are in r.header dict
"""print(r.headers['content-type'])
print(r.headers['Last-Modified'])
print(r.encoding)
print (r.text)
"""


def github_request (url='https://api.github.com'):
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

def github_request_pass_auth(url="https://api.github.com/repos/dejanu/linux/commits"):
    """request with user and pass as environ vars and
         query string parameters in the URL user params dict
            """
    u = os.environ["u"]
    p = os.environ["pas"]
    r = requests.get("https://api.github.com/repos/dejanu/linux/commits",params={'per_page': '100'}, verify=False,auth=HTTPDigestAuth(u,p))
    if r.status_code == 200:
        # get the content as  a list
        parsed = json.loads(r.content)
        return parsed

def gitlab_request(url,decoder = True):
        """GET request, default SSL verify=True
            and add headers """
        basic_request = requests.get(url, verify=False, headers={'PRIVATE-TOKEN':os.get['token']})
        if basic_request.status_code == 200:
            if decoder:
                return basic_request.json()
            else:
                # .content raw bytes of the response payload for string use .text
                return basic_request.content
        else:
            return None
if __name__ == "__main__":

    print(gitlab_request("https://gitlab.com/api/v4/projects/9395683/jobs"))
