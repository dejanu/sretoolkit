#!/usr/bin/python3

import json

from prometheus_client import Info, start_http_server
from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, InfoMetricFamily, REGISTRY

import requests
from requests.exceptions import HTTPError

class CustomCollector(object):

    @staticmethod
    def convert_to_metric(endpoint=None,json_file=False):
        """
        <metric name>{<label name>=<label value>, ...}
        """
        # json_file from disk
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
        yield GaugeMetricFamily('my_gauge', 'Help text', value=7)

        c = CounterMetricFamily('my_counter_total', 'Help text', labels=['fodo'])
        c.add_metric(['bar'], 123)
        c.add_metric(['baz'], 5435)
        yield c

        #d = CustomCollector.convert_to_metric(json_file="response.json")
        # d = CustomCollector.convert_to_metric(endpoint="http://servermonitor/health")

        i = InfoMetricFamily ("cura_plan_health_info", "Info about curaplan app")
        i.add_metric(['health_status'],  {'healthy': "TESTME", 'name': "yes"})
        # for c in range(len(d["services"])):
        #     print(c)
        #     i.add_metric(['healthy_status'],  {'app': str(d["services"][c]["name"]), 'status': str(d["services"][c]["healthy"])})
        
        yield i




if __name__ == "__main__":

    REGISTRY.register(CustomCollector())
    
    ## single time series
    # i = Info('cura_plan_health_info', 'Info about healthcheck')
    # i.info({'healthy': "TESTME", 'name': "yes"})
    
    start_http_server(8888)
