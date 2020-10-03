#!/usr/bin/env python

# The EXEC system call understands shebangs natively
# if ((bprm->buf[0] != '#') || (bprm->buf[1] != '!')) reads the very first bytes of the file, and compares them to #!
# if comparison is True the Linux kernel, which makes another exec call with path /usr/bin/env python and current file as the first argument


import os

print(os.listdir(os.getcwd()))

