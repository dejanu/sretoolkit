#!/usr/bin/python

import subprocess

## python 2.7 OLD OLD approach
from subprocess import Popen, PIPE
processs = Popen (["whoami"],stdin=PIPE, stdout=PIPE, stderr=PIPE)
output,err = processs.communicate()
print("Ouput is {0}".format(output))

#cannot capture the output in the script, it will be printed to stdout, you ll get only the return code
#get_return_code = os.system("env")

# shell=False  is set, there is no system shell started up., so the first argument must be a path to an executable file
#x = subprocess.run(["ls","-l"])


# shell=True will first spin up a system dependent shell process (commonly \bin\sh on Linux or cmd.exe on Windows) and run the command within it
#y = subprocess.run("ls -l",shell=True)

#get the output as bytes, shell=True means system shell \bin\sh will first spin up
#proc=subprocess.check_output("ls -l", shell=True)


#get the output as str
#proc = subprocess.run("ls -al", shell=True, encoding="utf-8", stdout=subprocess.PIPE)

#output = proc.stdout




if __name__ == "__main__":
	
	#list container names and images
	running_containers = subprocess.run("docker ps --format \'{{.Names}} {{.Image}}\'", shell=True, encoding="utf-8", stdout=subprocess.PIPE)
	

	#save the str cmd result as a list ["container image", "container image"]
	container_image = running_containers.stdout.strip().split("\n")
    

	
	ip_list = list()
	for i in container_image:
		r = (subprocess.run("docker inspect --format \'{{.NetworkSettings.IPAddress}}\' " + i.split(" ")[0], shell=True, encoding="utf-8", stdout=subprocess.PIPE))
		print (" {0} with ip: {1} ".format(i, r.stdout))

	
		


