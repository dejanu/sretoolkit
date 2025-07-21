#!/usr/bin/env python3
import os
def parse_logfile(file_path):
    """ parses the log file and returns a dict with number of lines, ERRORS and WARNINGS count"""
    file_info = {}
    print(f"File: {file_path}")

    with open(file_path,'r') as f:
            lines = f.readlines() # readlines() loads the entire file into memory. For large log files, this could be inefficient 
            file_info["Total lines"] = len(lines)
            file_info["ERRORs"] = " ".join(lines).count("ERROR")
            file_info["WARNINGs"] = " ".join(lines).count("WARNING")

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