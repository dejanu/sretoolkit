#!/usr/bin/python3

import concurrent.futures
import threading

import requests
import time

# parallelism = simultaneously for multicore
# concurency = specific kind of parallelism used for single core

## Multi-threading (concurency) when program is network bound - Threading is one of the most well-known approaches to attaining Python concurrency
## threads are used in cases where the execution of a task involves some WAITING

## Multi-processing when program is CPU bound
## processes are used for parallel CPU computation


thread_local = threading.local()

def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
