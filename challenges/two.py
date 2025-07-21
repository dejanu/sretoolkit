#!/usr/bin/env python3

import requests

endpoint = "https://api.open-meteo.com/v1/forecast?latitude=44.43&longitude=26.10&current_weather=true"

def get_weather_info(endpoint):
    """ extract temp, wind speed and time observation"""
    try:
        r = requests.get(endpoint)
        r.raise_for_status()
        data = r.json()
        print(f"Temp: {data.get('current_weather').get('temperature')}")
        print(f"Wind Speed: {data.get('current_weather_units').get('windspeed')}")
        print(f"Time of observation: {data.get('current_weather').get('time')}")
    except requests.exceptions.HTTPError as err:
        print("HTTP error:", err)
    except requests.exceptions.RequestException as err:
        print ("Other error", err) # i.e. ConnectionResetError

def post_to_http(endpoint,payload):
    """ post to endpoint """    
    try:
        r = requests.post(endpoint,json=payload)
        r.raise_for_status()
        print("Response:", r.json())
    except requests.exceptions.HTTPError as err:
        print ("HTTP err", err)
        
    return r

if __name__ == "__main__":

    #endpoint = "https://api.open-meteo.co/v1/forecast?latitude=44.43&longitude=26.10&current_weather=true"
    endpoint = "https://httpbin.org/post"


    #get_weather_info(endpoint)
    payload = { "name": "Alice", "role": "SRE", "skills":[1,2,3] }
    post_to_http(endpoint,payload)