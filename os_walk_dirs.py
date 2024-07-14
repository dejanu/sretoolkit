#!/usr/bin/env python3


import platform,getpass,socket,sys,os
import time

# Dumb method to get HOST ip and user
host_ip = socket.gethostbyname(socket.gethostname())
host_user = getpass.getuser()

        
# Set env variables
os.environ['API_USER'] = 'username'
# Get env variable
user = os.environ['API_USER'] # where os.environ return a dict with all env
user = os.environ.get('API_USER')
java_home = os.getenv("COMPUTERNAME","var not fond")                
    

def list_cdw():
    """ print absolute patth for each file from the cwd"""
    for (path,dirs,fils) in os.walk(os.getcwd()):
        for f in fils:
            print(os.path.join(path,f))
    
def listtimestamp():
    """ list files and timestamp"""
    for i in os.listdir(os.getcwd()):
        print (i, "Last Modified:" + time.ctime(os.path.getmtime(i)))
        print (i, "Created:" + time.ctime(os.path.getctime(i)))

def print_directory_contents(sPath):
    """
    This function takes the name of a directory 
    and prints out the paths files within that 
    directory as well as any files contained in 
    contained directories. 

    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your 
    ability to work with nested structures. 
    """
    dir_list=os.listdir(sPath)
    for files_and_dirs in dir_list:
        files_and_dirs_Path = os.path.join(sPath,files_and_dirs)
        if os.path.isdir(files_and_dirs_Path):
            #if we have a dir call recusion
            print_directory_contents(files_and_dirs_Path)
        else:
            print(files_and_dirs_Path)

def time_stamp():
    """get directory contents and print the file creation date"""
    for r,d,f in os.walk(os.getcwd()):
        for fisier in f:
            modification_time = time.ctime(os.path.getmtime(os.path.join(r,fisier)))
            print(str(modification_time) + fisier)
        
if __name__ == "__main__":

    #list_cdw()
    #listtimestamp()
    
    # ##when a module is loaded the __file__ is set to its name C:\\Users\\dej\\Desktop\\Git_projects\\Python\\os_platform_info.py
    # print(__file__)

    # ##you can use it to find the directory that the file is located
    # print(os.path.dirname(__file__))

    # ##avoid hardcoding the module absolute path
    # print(os.path.join(os.getcwd(),"OOP"))

    # verify if env var exists
    if os.getenv('PHIPROD_USER'):
        if os.getenv('PHIPROD_KEY'):
            print(f"Establish connection")
        else:
            sys.exit("Please set PHIPROD_KEY as env var")
    else:
        sys.exit("Please set PHIPROD_USER as env var")



