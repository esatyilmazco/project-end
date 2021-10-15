from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan

#connected elasticsearch
elasticConnect = Elasticsearch([{'host': '18.156.199.93', 'port': 9200}])

#pull value from user
findValue=input("which label in logs do you want?")

#example usage=findValue=kibana-efk(value entered in the input)
#which label in logs do you want?kibana-efk
#@log_name=kibana-efk 

def ElasticManagerApp(): 
    contentQuery = {
        "query": {
            "match": {
                #will search by entered value
                #filterer by @log_name
                "@log_name": findValue          
            }
        }
    }
    field = scan(client=elasticConnect,
        query=contentQuery,
        scroll='1m',
        index='fluentd*',
        raise_on_error=True,
        preserve_order=False,
        clear_scroll=True)
    resources = list(field)
    cluster = []
    for transformation in resources:
        cluster.append(transformation['_source'])
    return cluster

#call function
portForward=ElasticManagerApp()
print(portForward)
