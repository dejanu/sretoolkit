import sys , urllib.request
import ssl

# Fix URLError urlopen error SSL: Certifiacte Verify FALSE, prereq pip install certi
try:
   _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


try:
	rfc_number = int(sys.argv[1])
except (IndexError, ValueError):
	print('Must supply RFCnumber as first argument')
	sys.exit(2)


template = 'http://www.ietf.org/rfc/rfc{}.txt'
url = template.format(rfc_number)
rfc_raw = urllib.request.urlopen(url).read()
rfc = rfc_raw.decode()
print(rfc)
