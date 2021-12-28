#!/usr/bin/python

import sys
import re

def line_valid(line_no, line):
    """
    return True if line is ok
    """
    if line_no == 0:
        # first line should have the task idetifier e.g TASK-4351
        return re.match("^TASK-\d{1,5}.*", line)
 
def show_rules():
    """
    Rules for a great git commit message style
    """
    print("Please follow the rules add task/feature TASK-xxxx in the name of the commit msg""")

def main():
    print("Args are {}".format(sys.argv))
    # read commit-msg
    with open(sys.argv[1], "r") as fp:
        lines = fp.readlines()
        for l in lines:
            print(l)
        for line_no, line in enumerate(lines):
            #print(line_no,line)
            if not line_valid(line_no, line):
                show_rules()
                sys.exit(1)
    sys.exit(0)

if __name__=="__main__":
    main()
