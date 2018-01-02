from datetime import datetime

import json

ehosts=[]
eindex='dummy'
ebody=''
#es = Elasticsearch(['172.20.128.6'])
from elasticsearch import Elasticsearch

class Elasticpost:


    def post(self, ehost, eindex, etype, doc):
        """ a """
        
        esession = Elasticsearch(ehost)
        res = esession.index(eindex, etype, json.loads(doc))
        return res  


