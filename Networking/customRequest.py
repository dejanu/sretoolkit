## python3

## Adding headers to a request before sending it

from urllib.request import Request
from urllib.request import urlopen


req  = Request('http://debian.org')

## adding headers (header_name, header_value)
req.add_header('Accept-Language', 'sv')

response = urlopen(req)

print(response.read())
