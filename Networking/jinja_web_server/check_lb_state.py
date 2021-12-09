#!/usr/bin/python3

import requests
from requests.exceptions import HTTPError
from requests.auth import HTTPBasicAuth

def call_endpoint3(url):
    """
    3.x implementation for GET request to the endpoint
    """
    try:
        # without SSL certificate verification
        response = requests.get(url,auth=HTTPBasicAuth('user','password'),verify=False)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print("Success!")
    
        return response.json()


#def call_endpoint2(url):
#    """ 
#    2.7 implementation for GET request to the endpoint
#    """
#    import urllib2
#    import ssl
#
#    context = ssl._create_unverified_context()
#    
#    if url:
#        print(url)
#        req = urllib2.Request(url)
#        try:
#            response = urllib2.urlopen(req, context=context)
#        except urllib2.URLError, e:
#            print(e)
#            return e.reason
#
        #get response
#        request_text_response = response.read()
#        return response.getcode()



if __name__ == "__main__":
    
#   lb_state2 = call_endpoint2("http://mockbin.com/request?foo=bar&foo=baz")
    lb_state3 = call_endpoint3("http://mockbin.com/request?foo=bar&foo=baz")
