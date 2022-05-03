#!/usr/bin/env python3


from OpenSSL import crypto
from OpenSSL import SSL
from datetime import datetime
import os
from socket import socket, AF_INET, SOCK_STREAM
import ssl
import idna
import subprocess


# SSL context = collection of cipher,protocol versions, trusted certs, TLS options
# SSL session = each SSL connection involves one session at a time

def validate_cert(cert_file_path):
    """ check cert validity from local """

    if os.path.isfile(cert_file_path):

        with open(cert_file_path, "r") as f:
            cert_buf = f.read()
        cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert_buf)
        date_format, encoding = "%Y%m%d%H%M%SZ", "ascii"
        not_before = datetime.strptime(cert.get_notBefore().decode(encoding), date_format)
        not_after = datetime.strptime(cert.get_notAfter().decode(encoding), date_format)
        validity = f"Validity:\n Not Before: {not_before} \n Not After: {not_after}"
        return validity
    else:
        print(f"No cert file at {cert_file_path}")


def get_server_subject(host, port = 443):
    expected_subjects = []
    ctx = SSL.Context(method=SSL.SSLv23_METHOD)
    ctx.verify_mode = SSL.VERIFY_NONE
    ctx.check_hostname = False
    conn = SSL.Connection(ctx, socket(AF_INET, SOCK_STREAM))
    conn.connect((host, port))
    conn.settimeout(3)
    conn.set_tlsext_host_name(idna.encode(host))
    conn.setblocking(1)
    conn.set_connect_state()
    try:
        conn.do_handshake()
        expected_subjects :list[crypto.X509Name] = conn.get_client_ca_list()
    except SSL.Error as err:
        raise SSL.Error from err
    finally:
        conn.close()
    return expected_subjects


def cmd_wrapper(cmd):
    """ wrapper for cmds with pipe """
    if isinstance(cmd,str):
        proc = subprocess.Popen(cmd,stdin=subprocess.PIPE, shell=True)
        proc_stdout,proc_stderr = proc.communicate()
        return proc_stdout

if __name__ == "__main__":

    cert_path = "path/to//cluster/cluster.cer"
    host = "deployment.machine.com"
    port = 5443

    get_server_subject(host,port)
    print(validate_cert(cert_path))