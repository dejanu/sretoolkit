

# Text containg non-ASCII chars then use Unicode

# A python charactes is really a byte -> python string are really byte strings

# Converting from Unicode to byte string is ENCODING the string
# Load Unicode strings  -> decoding from bytes to char

# Convert Unicode to plain Python string: "encode"
unicodestring = u"Hello world"
utf8string = unicodestring.encode("utf-8")
asciistring = unicodestring.encode("ascii")
isostring = unicodestring.encode("ISO-8859-1")
utf16string = unicodestring.encode("utf-16")

# Convert plain Python string to Unicode: "decode"
plainstring1 = unicode(utf8string, "utf-8")
plainstring2 = unicode(asciistring, "ascii")
plainstring3 = unicode(isostring, "ISO-8859-1")
plainstring4 = unicode(utf16string, "utf-16")

assert plainstring1==plainstring2==plainstring3==plainstring4
