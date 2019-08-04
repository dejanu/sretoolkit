#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys, urllib.request

try:
	rfc_number = int(sys.argv[1])
except (IndexError, ValueError):
	print("Must supply RFC as first argument")
	sys.exit(2)

url = "http://www.ietf.org/rfc/rfc{}.txt".format(rfc_number)

rfc_raw = urllib.request.urlopen(url).read()

#convert from bytes to string
rfc = rfc_raw.decode()

print(rfc)
