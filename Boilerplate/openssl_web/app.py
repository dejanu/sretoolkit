#!/usr/bin/env python3

from flask import Flask, render_template
from openssl_wrapper import cmd_wrapper

app = Flask(__name__)

registry_list=["deployment.gultsundhedskort.dk","deployment.dev.phi.projects.systematic-synergy.io"]



@app.route("/")
def index():
    """entrypoint for index page"""
    #cmd = "openssl s_client -connect google.com:443 -showcerts |  openssl x509 -noout  -dates"
    cmd = "openssl s_client -connect deployment.gultsundhedskort.dk:5443 -showcerts |  openssl x509 -noout  -dates"
    cert_dates=cmd_wrapper(cmd).strip().split("\n")
    print(cert_dates)

    return render_template("index.html", cert_dates=cert_dates, registry=registry_list[0])