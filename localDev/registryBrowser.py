#!/usr/bin/python3

# curl -k -X GET https://<USER>:<PASSWORD>@index.docker.io/v2/_catalog
# docker search https://index.docker.io/grafana
# endpoints:
# /v2/_catalog 
# /v2/<IMAGE>/tags/list

import requests
import json
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import sys

from python_vault import *

warnings.simplefilter('ignore',InsecureRequestWarning)

def reg_inspect(reg=None, user=None, password=None):
    """ pprint all repositories and tags from registry"""

    #bad handshake: Error([('SSL routines)) - Fix me please
    try:
        catalog_url="https://{}:{}@{}/v2/_catalog".format(user,password,reg)
        response = requests.get(catalog_url, verify=False)
    except:
        catalog_url="http://{}:{}@{}/v2/_catalog".format(user,password,reg)
        response = requests.get(catalog_url, verify=False)
    for i in response.json().get("repositories"):
        try:
            tags_url="http://{}:{}@{}/v2/{}/tags/list".format(user,password, reg, i)
            print(i, json.dumps(requests.get(tags_url, verify=False).json(), indent=2))
        except:
            tags_url="https://{}:{}@{}/v2/{}/tags/list".format(user,password, reg, i)
            print(i, json.dumps(requests.get(tags_url, verify=False).json(), indent=2))


if __name__== "__main__":
    

    if len(sys.argv)!=4:
        print("Wrong number of args \t  --> ./registryBrowser.py  <registry_url> <user> <registry_password> \n")
    else:
        reg_inspect(reg=sys.argv[1],user=sys.argv[2],password=sys.argv[3])
