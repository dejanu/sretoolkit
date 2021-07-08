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

from python_vault import decrypt_it

warnings.simplefilter('ignore',InsecureRequestWarning)

# mock encrypted_passwords
reg_dict = { "registry1_user":b'gym01qQ==' ,
            "registry2_user": b'gAAAAABQ==' ,
            "registry3_user":b'gAAAdf_E=' ,
        }

# endpoints:
# /v2/_catalog 
# /v2/<IMAGE>/tags/list

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

def fermet_reg_inspect(reg=None, user=None, fernet_key=None):
    """ pprint all repositories and tags from registry using encryption"""

    print(user)
    encoded_password = reg_dict.get(user,"User not found")
    print(encoded_password)
    # convert back to str to avoid simplejson.errors.JSONDecodeError
    password = decrypt_it(encoded_password,fernet_key).decode("utf-8")
    print(password)

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
    
    
    # if len(sys.argv)!=4:
    #     print("Wrong number of args \t  --> ./registryBrowser.py  <registry_url> <user> <password> \n")
    #     print("e.g.: ./registryBrowser.py  internal-reg:25001 <user>  <password>")
    # else:
    #     reg_inspect(reg=sys.argv[1],user=sys.argv[2],password=sys.argv[3])

    if len(sys.argv)!=4:
        print("Wrong number of args \t  --> ./registryBrowser.py  <registry_url> <user> <key> \n")
        print("e.g.: ./registryBrowser.py  internal-reg:25001 <user>  <key>")
    else:
        fermet_reg_inspect(reg=sys.argv[1],user=sys.argv[2],fernet_key=sys.argv[3])

