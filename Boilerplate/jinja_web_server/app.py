#!/usr/bin/env python3

import os

from check_lb_state import call_endpoint3

from flask import Flask, render_template
app = Flask(__name__)

def create_pid_file():
    """get the current process (current script) pid and write it to /tmp"""

    pid = str(os.getpid())

    # script name as pid_file
    pid_file = os.path.basename(__file__)

    pidfile_abs_path = "{}/{}.pid".format(os.getcwd(),pid_file[:len(pid_file)-3])
    print(pidfile_abs_path)
    with open(pidfile_abs_path,"w") as f:
        f.write(pid)
    return pidfile_abs_path

@app.route("/")
def index():
    """entrypoint for index page"""
    # read url as environment variable
    lb_url = os.environ.get("LB_URL")
    if not lb_url:
        lb_url = "http://mockbin.com/request?foo=bar&foo=baz"
        
    lb_state = call_endpoint3(lb_url)
    
    # dict object to be used in render_template
    pools_state = lb_state.get("state").get("pools")
    
    # pass pools as list
    return render_template("index.html",pools_sts=pools_state)

@app.route("/status", methods=['GET', 'POST'])
def status():
    """status page"""
    # read url as environment variable
    lb_url = os.environ.get("LB_URL")
    if not lb_url:
        lb_url = "http://mockbin.com/request?foo=bar&foo=baz"
        
    lb_state = call_endpoint3(lb_url)
    
    # get errors as list
    err_sts = lb_state.get("state").get("errors")
    return render_template("status.html",sts=err_sts)

if __name__ == "__main__":
    try:
        pidfile = os.path.basename(__file__)
        os.unlink("{}/{}.pid".format(os.getcwd(),pidfile[:len(pidfile)-3]))
    except OSError:
        print("Pid file not found")

    pid_file = create_pid_file()

    app.run(host='0.0.0.0', port=9095, debug=True)
