#!/usr/bin/python3

from urllib.request import urlopen
import ssl

import requests
from requests.exceptions import HTTPError

try:
   _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


# # Get response object
# response = urlopen('http://www.debian.org')
# print ("Requested url is: {} and the status code is {}".format(response.url, response.status))

# # get the http headers (header_name, header_value)
# print (response.getheaders())

# ## using the file interface to read the response and retrieve only 50 Bytes of data
# ## response.read() and response.readline() return bytes objects and http and urllib do not decode the received data into Unicode
# print(response.read(50))

def call_endpoint(url,insecure=True):
    """
    This function calls the endpoint and returns the response
    """
    try:
        if insecure:
            # without SSL certificate verification
            response = requests.get(url, verify=False)
        else:    
            response = requests.get(url,auth=('user','pass'))
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print("Success!")


if __name__ == "__main__":
	pass
