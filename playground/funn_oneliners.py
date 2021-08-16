#!/usr/bin/env python

# The EXEC system call understands shebangs natively
# if ((bprm->buf[0] != '#') || (bprm->buf[1] != '!')) reads the very first bytes of the file, and compares them to #!
# if comparison is True the Linux kernel, which makes another exec call with path /usr/bin/env python and current file as the first argument

# oneliner oneliners

#fibonacci
fib = lambda n: n if n < 2 else (fib(n - 1) + fib(n - 2))

#gotcha get ip
import socket
socket.gethostbyname(socket.gethostname())


## Start a simple webserver running in the background on port 8000 with the current directory as the doc root
## sending stdout and stderr to /dev/null. Also making sure it continues running when the shell is closed.
nohup python3 -m http.server 80 > /dev/null 2>&1 & 
# ptyhon 2
python -m SimpleHTTPServer 80


#quine - no input and produces a copy of its own source
#%s prints the str() of an object (What you see when you print(object)).
#%r prints the repr() of an object (What you see when you print(repr(object))
s='s=%r;print(s%%s)';print(s%s)
