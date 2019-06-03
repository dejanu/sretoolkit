#!/usr/bin/python

## Update config for jump host server

from subprocess import Popen,PIPE
import sys, os, getpass


def call_proc(*args):
        """ dumb 2.7 """
        args_list = list()
        for i in args:
                args_list.append(i)
        proc = Popen(args_list,stdin=PIPE,stdout=PIPE,stderr=PIPE)
        proc_stdout,proc_stderr = proc.communicate()
        return proc_stdout


def create_config(private-key = "id_rsa", remote_server = None):
        """ create configuration file for jump server """
        
        if remote_server:
                stepping_stone ="""Host jump_server
                User {0}
                HostName 12.345.67.89
                IdentitiesOnly yes
                IdentityFile /home/{0}/.ssh/{1}\n\n""".format(getpass.getuser(), private-key)
        
                node  = """Host {1}
                User {0}
                Hostname {2}.domain
                ProxyCommand ssh -q -W %h:%p clrv0000068290.ic.ing.net\n\n""".format(getpass.getuser(),remote_server)
        

        # write ssh config
        os.chdir(r"/home/{0}/.ssh".format(getpass.getuser())
        with open("config","w") as f :
                f.write(stepping_stone)
                f.write(node)


