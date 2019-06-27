#!/usr/bin/python

from subprocess import PIPE, Popen
import os

def call_procc(cmd=None):
	""" 2.7 call process
	return output as str"""
	if cmd:
		cmd_list = cmd.split(" ")
		process = Popen(cmd_list, stdin = PIPE, stderr = PIPE, stdout = PIPE)
		output,stderr = process.communicate()
		return output

def get_binaries():
	"""curl for runner bin
	   return sys code"""
	#check if binaries are on local
	if call_procc("find /usr/local/bin/ -name gitlab-runner"):
		print("runner binaries installed")
		return os.system("chmod +x /usr/local/bin/gitlab-runner")
	else:
		return os.system("curl -L --output /usr/local/bin/gitlab-runner https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-linux-amd64")

def user_create():
	"""create gitlab-runner user and run it as service"""
	
	if os.system("useradd --comment 'GitLab Runner' --create-home gitlab-runner --shell /bin/bash") == 0:
		print(call_procc("gitlab-runner install --user=gitlab-runner --working-directory=/home/gitlab-runner"))
		os.system("gitlab-runner start")
	else:
		print("gitlab-runner user present")
		print(os.system("/usr/local/bin/gitlab-runner install --user=gitlab-runner --working-directory=/home/gitlab-runner"))
		os.system("/usr/local/bin/gitlab-runner start")
	

if __name__ == "__main__":

	print(get_binaries())
	user_create()
