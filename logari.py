#!/usr/bin/python

import logging
import os

### Logging LEVELS ##
#####################
## DEBUG
## INFO
## WARNING (default)
## ERROR
## CRITICAl

def print_to_console(LogLevel=10, mymessage="insert log message here"):
	""" LogLevel: int  warning, info,debug etc, the INFO will not appear to console  because WARNING is default"""
	
	if LogLevel == 10:
		logging.debug(mymessage)
	elif LogLevel == 20:
		logging.info(mymessage)
	elif LogLevel == 30:
		logging.warning(mymessage)
	elif LogLevel == 40:
		logging.error(mymessage)
	elif LogLevel == 50:
		logging.critical(mymessage)

def log_to_file(logfile):
	""" log to a file """
	# create loggin instance
	#	logger =  logging.getLogger(__name__)
	
	LOG_FORMAT = "%(levelname)s %(asctime)s %(message)s"
	print(os.getcwd())
	logging.basicConfig(filename=str(os.chdir("/var/log/pythonlog"))+logfile,filemode="w",  level=logging.DEBUG, format=LOG_FORMAT)
	
	# log 2 file
	logging.debug("This should go to log file")
	
if __name__ == "__main__":
	    
	log_to_file("lelogs.log")

	print_to_console(30,"dafaq man")
