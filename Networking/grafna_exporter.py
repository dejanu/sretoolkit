#!/usr/bin/env python

# There are two ways to autheticate to grafana api: api token or basic auth.
# docs: https://grafana.com/docs/grafana/latest/http_api/dashboard/

import sys,os
import requests
from requests.exceptions import HTTPError

import ssl
context = ssl._create_unverified_context()

import json
from subprocess import Popen, PIPE


def get_dashboards(grafana_instance=None):
    """ wrapper /api/search get request without auth"""

    if isinstance(grafana_instance,str):
        grafana_search="{}/api/search".format(grafana_instance)
        try:
            response = requests.get(grafana_search,verify=False)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
        else:
            print('Success!')

            ## MUCH WOW MUCH OPTIONS
            # return message body content as  bytes
            #return response.content

            # return message body content as  string
            #return response.text

            # return message body as dict/json or list 
            #return json.loads(response.text)

            # return using requests built-in
            return response.json()


def get_dashboard(grafana_instance=None, dashboard_uid=None):
    """ wrapper /api/dashboards/uid/<UID> get request without auth"""
    if grafana_instance and dashboard_uid:
        dashboard_search="{}/api/dashboards/uid/{}".format(grafana_instance,dashboard_uid)
        try:
            response = requests.get(dashboard_search,verify=False)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
        else:
            print('Success!')

            return response.json()

def post_dashboard(grafana_instance=None, dashboard_json=None):
    """ wrapper for POST /api/dashboards/db"""
    dashboard_post="{}/api/dashboards/db/".format(grafana_instance)
    
    dashboard_json = 
    r = requests.post('{}'.format(dashboard_post), dashboard_json={"key": "value"})

    return r.status_code

if __name__ == "__main__":

            # list of dashboards dash-db UIDs 
            x = list(map(lambda x: (x.get("uid"),x.get("title")) if x.get("type")=="dash-db" else None, get_dashboards(grafana_instance="https://localhost:3000")))

            a = get_dashboard(grafana_instance="https://localhost:3001",dashboard_uid="radnoms54ing")

            # serialize dict to json 
            a_dict = a.get("dashboard")
            with open("t.json","w") as f:
                f.write(json.dumps(a_dict))

            
