#!/usr/bin/python3

# parallelism = simultaneously for multicore
# concurency = specific kind of parallelism used for single core

## Multi-threading (concurency) when program is network bound - Threading is one of the most well-known approaches to attaining Python concurrency
## threads are used in cases where the execution of a task involves some WAITING

## Multi-processing when program is CPU bound
## processes are used for parallel CPU computation


import time
import requests

import concurrent.futures
import threading


thread_local = threading.local()

#def call_tenant(url,session):
#    with session.get(url) as response:
#        return response.content

def call_tenant(url,session):
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


#def call_all_tenants(urls):
#    with requests.Session() as session:
#       for url in urls:
#           print(call_tenant(url,session))
def call_all_tenants(urls):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(call_tenant, urls)


if __name__ == "__main__":

    urls=["endpoints"]

    call_all_tenants(urls)
    print(f"Downloaded {len(sites)} in {duration} seconds")
