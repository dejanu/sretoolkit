#!/usr/bin/python



import os
import sys
import time
import psutil




def create_pid_file():
	"""get the current process (current script) pid and write it to /tmp"""
	
	# echo $$ or pid = fork()	
	pid = str(os.getpid())
	
	# script name as pid_file
	pid_file = os.path.basename(__file__)
	pid_file_alternative = sys.argv[0]
	
	pidfile_abs_path = "/tmp/{}.pid".format(str(pid_file)) 
	print(pidfile_abs_path)
	
	# check if proc is running via pidfile_abs_path exists
	if os.path.isfile(pidfile_abs_path):
		print ("pid file existing")
		
		#check if the proc is running via PID
		# if psutil.pid_exists(os.getpid())
		sys.exit()
	else:
		# write pid file
		with open(pidfile_abs_path,"w") as f:
			f.write(pid)
	
	#sleep 10 sec
	time.sleep(10)
	### IMPLEMENT LOGIC###	

	#remove pidfile path
	os.unlink(pidfile_abs_path)

if __name__ == "__main__":

	
	create_pid_file()
