#!/usr/bin/python3

from prometheus_client import Info, make_wsgi_app
from wsgiref.simple_server import make_server
from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, InfoMetricFamily, REGISTRY

import requests
import json
from requests.exceptions import HTTPError

"""
# view child processes
pgrep -P $(ps -C containerd | awk 'FNR == 2 {print $1}')  
pstree $(ps -C containerd)

ps -p 2281 -o comm=

for i in $(ps -C containerd | awk 'FNR > 1 {print $1}');do pstree $i;done

containerd-shim is a child process of containerd that serves a single container and takes care of the container lifecycle and exposes its functions to containerd through containerd-shim API
containerd  - containerd runtime, your images are built in the standardised Open Container Initiative (OCI) - available as a daemon for Linux 


"""
class CustomCollector(object):

    @staticmethod
    def convert_to_metric(endpoint=None,json_file=False):
        """
        cd /pack/monitoring/services/prometheus_normal/etc/file_sd/plan.json
        curl -s http://URL
        """
        # read json_file from disk
        if json_file:
            f = open(json_file,'r')
            metric  = json.load(f)
            f.close()
            return metric
        # curl endpoint
        else:
            try:
                response = requests.get(endpoint,verify=False) # disable TLS certificate verification
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
            except Exception as err:
                print(f'Other error occurred: {err}')
            else:
                print('Success!')

                ## MUCH WOW MUCH OPTIONS (**)
                # return message body content as  bytes
                #return response.content

                # return message body content as  string
                #return response.text

                # return message body as dict/json or list 
                #return json.loads(response.text)

                # return using requests built-in
                return response.json()


    def collect(self):
        yield GaugeMetricFamily('running_containers', 'gauge', value=7)

        c = CounterMetricFamily('my_counter_total', 'Help text', labels=['test'])
        c.add_metric(['bar'], 123)
        c.add_metric(['baz'], 5435)
        yield c

        #d = CustomCollector.convert_to_metric(json_file="response.json")
        #d = CustomCollector.convert_to_metric(endpoint="URL/health")

        # single time series
        i = InfoMetricFamily ("plan_health_info", "Info about plan app")
        i.add_metric(['health_status'],  {'healthy': "True", 'name': "Test app"})
        # for c in range(len(d["services"])):
        #     i.add_metric(['health_status'],  {'service': str(d["services"][c]["name"]), 'healthy': str(d["services"][c]["healthy"])})
        
        yield i



if __name__ == "__main__":

    REGISTRY.register(CustomCollector())
    app = make_wsgi_app()
    httpd = make_server('', 8888, app)
    httpd.serve_forever()



    
