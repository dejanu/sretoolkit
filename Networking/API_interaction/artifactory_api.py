
#!/usr/bin/python

# urllib2 can accept a Request object to set the headers for a URL request, 
# urllib accepts only a URL

### Usage GET/PUT

# curl -u dejanualexandru@gmail.com:passwd@ -X PUT "https://dej.jfrog.io/artifactory/pypi-local/" -T quine.py
# curl -k -O -u dejanualexandru@gmail.com:Alex123@ https://dej.jfrog.io/artifactory/pypi-local/quine.py

# curl -H "X-JFrog-Art-Api:insertapikeyhere"

# # Using your JFrog URL 
# http://myjfrog.acme.org/artifactory/
 
# # Using your Artifactory server hostname and port
# http://ARTIFACTORY_SERVER_HOSTNAME:8081/artifactory/

import os

# python2
#import requests
#from requests.auth import HTTPBasicAuth

# python2
#import urllib2

# python3
import urllib.request
import ssl
context = ssl._create_unverified_context()

def download_artifact3(url=None, filename=None):
    """ python3 urllib usage """
    if isinstance(url,str) and filename:

        request = urllib.request.Request(url.strip())
        request.add_header("X-JFrog-Art-Api", "insertapikeyhere")

        with urllib.request.urlopen(request,context=context) as response, open(filename, 'wb') as out_file:
            data = response.read() # a `bytes` object
            out_file.write(data)
    else:
        print("provide URL")


def download_artifact22(url=None, filename=None):
    """ python2 urllib2 usage """
    if isinstance(url,str) and filename:
        response = urllib2.urlopen(url.strip())
        dump = response.read()
        with open (filename, "wb") as f:
            f.write(dump)
        print("download {}".format(filename))
    else:
        print("Provide URL")

def download_artifact2(url=None, filename=None):
    """request usage"""
    if isinstance(url,str) and filename:
        response = requests.get(url.strip(), verify=False, auth=HTTPBasicAuth('dejanualexandru@gmail.com', 'passwd')) 
        # using token
        #response = requests.get(url, verify=False, headers={'PRIVATE-TOKEN':os.get['token']})

        if response.status_code == 200:
            #response content as  bytes
            with open(filename, 'wb') as f:
                for chunk in response.iter_content():
                    f.write(chunk)
        else:
            return response.status_code
    else:
        print("provide url")


if __name__ == "__main__":

    download_artifact3("https://dej.jfrog.io/artifactory/pypi-local/quine.py", "quine3.py")