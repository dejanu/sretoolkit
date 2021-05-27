#!/usr/bin/env python

#There are two ways to autheticate to grafana api: api token or basic auth.
#docs: https://grafana.com/docs/grafana/latest/http_api/dashboard/

import sys,os
import requests
from requests.exceptions import HTTPError

import ssl
context = ssl._create_unverified_context()

import json
from subprocess import Popen, PIPE


def create_ApiToken(grafana_instance = None, keyName = None, user="admin", user_password="admin"):
    """ wrapper for POST to /api/auth/keys """
    if isinstance(grafana_instance,str):

        # effin url format
        creds = f"//{user}:{user_password}@"
        grafana_instance_creds = grafana_instance.replace("//",creds) 
        grafana_url="{}/api/auth/keys".format(grafana_instance_creds)

        print("Call to url: {}".format(grafana_url))

        # construct POST request as per docs
        r = requests.post(grafana_url, json={"name": keyName, "role": "Admin"}, headers={"Content-Type":"application/json"})
        
        if r.status_code == 200:
            return r.json()
        else:
            print(r.status_code)
            return r.text

def get_dashboards(grafana_instance=None):
    """ wrapper for GET /api/search without auth"""
    
    if isinstance(grafana_instance,str):
        grafana_search="{}/api/search".format(grafana_instance)
        try:
            response = requests.get(grafana_search,verify=False) # disable TLS certificate verification
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
        else:
            print('Success!')

            ## MUCH WOW MUCH OPTIONS (**)
            # return message body content as  bytes
            #return response.content

            # return message body content as  string
            #return response.text

            # return message body as dict/json or list 
            #return json.loads(response.text)

            # return using requests built-in
            return response.json()


def get_dashboard(grafana_instance=None, dashboard_uid=None):
    """ wrapper for GET /api/dashboards/uid/<UID> without auth"""
    if grafana_instance and dashboard_uid:
        dashboard_search="{}/api/dashboards/uid/{}".format(grafana_instance,dashboard_uid)
        try:
            response = requests.get(dashboard_search,verify=False) # diasble TLS certificate verification
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
        else:
            print('Success!')

            return response.json()

def post_dashboard(grafana_instance=None, user="admin", user_password="admin", api_key=None, apidashboard_json=None):
    """ wrapper for POST /api/dashboards/db"""
    
    if isinstance(grafana_instance,str):

        # effin url format
        creds = f"//{user}:{user_password}@"
        grafana_instance_creds = grafana_instance.replace("//",creds) 
        grafana_url="{}/api/dashboards/db".format(grafana_instance_creds)

        print(grafana_url)

        headers = {"Content-Type": "application/json","Authorization": f"Bearer {api_key}"}
        with open(apidashboard_json) as f:
            dashboard_data = json.load(f)
    
        r = requests.post(grafana_url, json=dashboard_data, headers=headers )
        print(r.status_code)

if __name__ == "__main__":


            # create local dir for exporting dashboards
            os.mkdir("{}{}{}".format(os.getcwd(),os.sep,"lesdashboards"))

            

            # list of dashboards dash-db UIDs 
            dashboard_list = list(map(lambda x: (x.get("uid"),x.get("title")) if x.get("type")=="dash-db" else None, get_dashboards(grafana_instance="http://localhost:3000")))

            # for API import
            #a = get_dashboard(grafana_instance="http://localhost:3000",dashboard_uid="dashboard_uid")

            # for GUI  import
            #a_dict = a.get("dashboard")
            # with open("t.json","w") as f:
            #     f.write(json.dumps(a))

            if os.path.exists("{}{}{}".format(os.getcwd(),os.sep,"lesdashboards")):
                os.chdir("lesdashboards")

            #serialize dashboards
            for dashboard in dashboard_list:
                # Not None for folders
                if dashboard:
                    print(f"Exported dashboard: {dashboard[1]}")
                    
                    d = get_dashboard(grafana_instance="http://localhost:3000",dashboard_uid=dashboard[0])
                    
                    # overwrite id to null in order to create dashboard
                    d["dashboard"]["id"]="null"
                    # serialize dict to json - uid as file name
                    with open(f"{dashboard[0]}.json", "w") as f:
                        f.write(json.dumps(d)) 

            # # create API token 
            pythonKey = create_ApiToken(grafana_instance="http://localhost:3000",keyName="pythonKey",user_password="admin")

            ## upload all dashboards from lesdashboard dir
            # print(pythonKey)
            for i in  os.listdir():
                post_dashboard(grafana_instance="http://localhost:3001",user="admin", user_password="admin", api_key=pythonKey.get("key"), apidashboard_json=i)
