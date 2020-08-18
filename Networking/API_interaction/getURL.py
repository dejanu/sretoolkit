
## python3

from urllib.request import urlopen
import ssl

try:
   _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


# Get response object
response = urlopen('http://www.debian.org')

print ("Requested url is: {} and the status code is {}".format(response.url, response.status))

# get the http headers (header_name, header_value)

print (response.getheaders())

# using the file interface to read the response and retrieve only 50 Bytes of data
print(response.read(50))  ## response.read() and response.readline() return bytes objects and http and urllib do not decode the received data into Unicode



if __name__ == "__main__":
	print(response)

