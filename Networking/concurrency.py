#!/usr/bin/python3

# parallelism = simultaneously for multicore
# concurency = specific kind of parallelism used for single core

## Multi-threading (concurency) when program is network bound - Threading is one of the most well-known approaches to attaining Python concurrency
## threads are used in cases where the execution of a task involves some WAITING

## Multi-processing when program is CPU bound
## processes are used for parallel CPU computation

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
    # create pool of threads to run concurrently
    ## prometheus instrumentation: <metric name>{<label name>=<label value>, ...}
    global g
    g = Gauge("tenant_health_status","health status of tenant",["tenant","status"])
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # control how/when each thread in the pool will run
        executor.map(call_tenant, urls)


if __name__ == "__main__":

    urls=["INSERT_URLS_LIST"]
    start_time = time.time()

    call_all_tenants(urls)

    duration = time.time() - start_time
    print (f"Time duration: {duration} seconds")

    ##create WSGI app
    app = make_wsgi_app()
    httpd = make_server('',8888, app)
    httpd.serve_forever()
