#!/usr/bin/python3
# https://tenthousandmeters.com/tag/python-behind-the-scenes/
"""
# view child processes
pgrep -P $(ps -C containerd | awk 'FNR == 2 {print $1}')  
pstree $(ps -C containerd)

ps -p 2281 -o comm=

for i in $(ps -C containerd | awk 'FNR > 1 {print $1}');do pstree $i;done

containerd-shim is a child process of containerd that serves a single container and takes care of the container lifecycle and exposes its functions to containerd through containerd-shim API
containerd  - containerd runtime, your images are built in the standardised Open Container Initiative (OCI) - available as a daemon for Linux 


"""
from prometheus_client import Info,Gauge
from prometheus_client.core import InfoMetricFamily

import time
import requests
import concurrent.futures
import threading

from prometheus_client import make_wsgi_app
from wsgiref.simple_server import make_server

thread_local = threading.local()

def get_session():
    """ return session obj that allows to persist params across requests"""
    if not hasattr(thread_local, "session"):
        # each thread will create its own session object
        thread_local.session = requests.Session()
    return thread_local.session

def call_tenant(url):
    """ call endpoint and extract/retrun desired info as str"""
    session = get_session()
    with session.get(url) as response:
        #print(response.content) - check the top-level key health:true
        g.labels(tenant=url, status=response.json().get("healthy", "service notfound")).inc()

def call_all_tenants(urls):
    """prometheus instrumentation: <metric name>{<label name>=<label value>,}"""
    # create pool of threads to run concurrently
    global g
    g = Gauge("tenant_health_status","health status of tenant",["tenant","status"])
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # control how/when each thread in the pool will run
        executor.map(call_tenant, urls)

def read_config(conf_file):
    """ read config file with endpoints"""
    with open(conf_file,"r") as f:
        lines = [l.rstrip() for l in f.readlines()]
    return lines

if __name__ == "__main__":

    urls=read_config("endpoints")
    start_time = time.time()

    call_all_tenants(urls)

    duration = time.time() - start_time
    print (f"Time duration: {duration} seconds")

    ##create WSGI app
    app = make_wsgi_app()
    httpd = make_server('',8888, app)
    httpd.serve_forever()



    
