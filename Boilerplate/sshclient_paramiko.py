#!/usr/bin/python

###fucking dumb way
##import pip
##
##pkgs = ['paramiko', 'jumpssh']
##for p in pkgs:
##    try:
##        import p
##    except ImportError:
##        pip.main(['install', p])
##        import paramiko
##        from jumpssh import SSHSession

import paramiko
import getpass


def ssh_to_server(command = None, remote_server = None, user_name = None, use_password = True):
    """ create SSH client """
    
    # set user as whoami if None is passed
    if not user_name:
        user_name = getpass.getuser()
 
    if not isinstance (command,str):
        raise ValueError("The command should be of type string")
    else:
        if use_password == True:
            client = paramiko.SSHClient()
            
            #Set policy to use when connecting to servers without a known host key aka Server  not found in known_hosts
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            client.connect(remote_server, port=2220, username = user_name , password = "bandit0")
            stdin, stdout, stderr = client.exec_command(command)
            result = stdout.readlines()
            client.close()
            return result
        
        else:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            #Set policy to use when connecting to servers without a known host key aka Server  not found in known_hosts
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            SSH_pub_key = "/home/{0}/.ssh/{1}".format(user_name,"lab")
	    # key_filename = str private_key or certs for authetication
	    client.connect(remote_server, port = 22 , username = user_name, key_filename = SSH_pub_key) 
            stdin, stdout, stderr = client.exec_command(command)
            result = stdout.readlines()
            print(result)
            client.close()
            return result
 

def ssh_jumpserver_to_server():
    """ create SSH client with jump server"""
    from jumpssh import SSHSession
    # establish ssh connection between your local machine and the jump server
    gateway_session = SSHSession('steppingstone','my_user', password='my_password').open()
    # from jump server, establish connection with a remote server
    remote_session = gateway_session.get_remote_session('remote.example.com',password='my_password2')
    
    #execute command on end server
    remote_session.get_cmd_output('ls -lta')

if __name__ == "__main__":
    x = ssh_to_server("id","192.168.0.59", use_password = False)
    print(x)
