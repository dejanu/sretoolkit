#!/usr/bin/env python3

import requests
from flask import Flask, render_template

from prometheus_client import Gauge, generate_latest

from urllib3.exceptions import InsecureRequestWarning
# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def read_config(config_file):
    """
    config_file: str - name of the config file wich resides in /tmp/
    """
    try:
        with open(f"/tmp/{config_file}","r") as f:
            lines = [l.rstrip() for l in f.readlines()]
        return lines
    except FileNotFoundError:
        raise FileNotFoundError(f"File {config_file} not found in /tmp/")


class myMetrics:

    def __init__ (self, cluster_base_domain):
        self.cluster_base_domain = cluster_base_domain
        self.vault_url = f"https://vault.admin.{cluster_base_domain}/v1/sys/health"
        self.registry_url = f"https://registry.admin.{cluster_base_domain}/api/v2.0/health"
        self.console_url = f"https://idp.admin.{cluster_base_domain}/auth/admin/synergy/console/"
    
    @staticmethod
    def curl_endpoint(url, with_json=True):
        """
        url: url str to curl
        with_json: True/False return body as json/unicode text 
        """
        print("Calling endpoints...")
        try:
            r = requests.get(url, verify=False)  # Disable TLS certificate verification
            r.raise_for_status()  # Raise an exception for non-successful status codes 
            if with_json:     
                return r.json(), r.status_code
            else:
                return r.text, r.status_code
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None, None
    
    def get_vault_status(self):
        """Get vault status"""
        body, status_code = self.__class__.curl_endpoint(self.vault_url)
        print(body)
        if status_code == 200:
            if (body.get("initialized")==True) and (body.get("sealed")==False):
                self.vault_status = "healthy"
            else:
                self.vault_status = "unhealthy"
        else:
            self.vault_status = "unhealthy"
        return self.vault_status

    def get_registry_status(self):
        """Get registry status"""
        body, status_code = self.__class__.curl_endpoint(self.registry_url)
        print(body)
        # self.registry_status["core"] = body.get("components")[1].get("status")
        # self.registry_status["registry"] = body.get("components")[6].get("status")
        if status_code == 200:
            if body.get("status") == "healthy":
                self.registry_status = "healthy"
            else:
                self.registry_status = "unhealthy"
        else:
            self.registry_status = "unhealthy"

        return self.registry_status
    
    def get_console_status(self):
        """Get console status"""
        _ , status_code = self.__class__.curl_endpoint(self.console_url, with_json=False)
        if status_code == 200:
            self.console_status = "healthy"
        else:
            self.console_status = "unhealthy"
        return self.console_status

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/index')
def index():
    """ Home page """
    return render_template('home.html')

@app.route('/metrics')
def metrics():
    """ Return promethues metrics """
    return generate_latest()

@app.errorhandler(500)
def handle_500(error):
    return str(error), 500

if __name__ == "__main__":

    # create gauge metric       
    g = Gauge('synergy_components', 'Gauge metric for Synergy main components',['cluster','vault','registry','console'])
    # if at least one component is unhealthy, the gauge will be 0
    # g.labels(....).set(0)

    g.labels(cluster=dev.cluster_base_domain, vault=dev.get_vault_status(), registry=dev.get_registry_status(), console=dev.get_console_status()).set_function(lambda: 0 if dev.get_vault_status() != "healthy" else 1)
    g.labels(cluster="mamita", vault=dev.get_vault_status(), registry=dev.get_registry_status(), console=dev.get_console_status()).set_function(lambda: 0 if dev.get_vault_status() != "healthy" else 1)
    
    # create Metrics object for each cluster defined in the config file
    for i in config:
        cluster_obj = myMetrics(i)
        # if at least one component is unhealthy, the gauge will be 0
        g.labels(cluster=cluster_obj.cluster_base_domain, vault=cluster_obj.get_vault_status(), registry=cluster_obj.get_registry_status(), console=cluster_obj.get_console_status()).set_function(lambda: 0 if cluster_obj.get_vault_status() != "healthy" else 1)
        # g.labels(....).set(0)
    
    app.run(host='0.0.0.0', port=8088)