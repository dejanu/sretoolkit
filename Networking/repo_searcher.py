#!/usr/bin/env python



# curl -k -X GET https://<USER>:<PASSWORD>@index.docker.io/v2/_catalog
# docker search # docker search https://index.docker.io/grafana

import sys,os 
import requests
from requests.exceptions import HTTPError

import ssl
context = ssl._create_unverified_context()

import json
from subprocess import Popen, PIPE

def get_repositories(username=None,password=None,registry=None):
    """ list repositories/images from registry"""
    registry_url = "https://{}:{}@{}/v2/_catalog".format(username,password,registry)

    try:
        response =  requests.get(registry_url, verify=False)
    #response.status_code == 200:
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
        #return message body content as  bytes
        #return response.content

        #return message body content as  string
        return response.text

def get_tags(registry=None, image_name=None):
    """ wrapper for docker CLI """
    process = Popen(['docker', 'search', '{}}/{}'.format(registry, image_name)], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    return stdout

if __name__ == "__main__":

    # convert to dict
    a = json.loads(get_repositories())
    



