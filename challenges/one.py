#!/usr/bin/env python3
import os
def parse_logfile(file_path):
    """ parses the log file and returns a dict with number of lines, ERRORS and WARNINGS count"""
    file_info = {}
    print(f"File: {file_path}")
    f = open(file_path,'r')
    c = 0
    e = 0
    w = 0
    for line in f.readlines():
        c+=1
        if "ERROR" in line:
            e +=1
        elif "WARNING" in line:
            w+=1
        else:
            pass
    
    file_info["Total lines"] = c
    file_info["ERROR"] = e
    file_info["WARNING"] = w
    # with open(file_path,r) as f:
    #         file_info["Total lines"] = len(f.readlines())
    #         file_info["ERRORs"] = 
    #         file_info["WARNINGs"] =

    return file_info

if __name__ == "__main__":
    print(f"Analyzing logs in {os.getcwd()}")
    # recurse list files in cwd
    for (path,dir,files) in os.walk(os.getcwd()):
        for f in files:
            # print abs path for 
            log_file = os.path.join(path,f)
            # check if file end with log extension
            if log_file.endswith("log"):
                for k,v in parse_logfile(log_file).items():
                    print(f'{k}: {v}')