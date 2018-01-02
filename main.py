"""
TODO: Name the App
"""

import time, json, threading
from flask import Flask
from flask_restful import Resource, Api
from igor.memstat import Memstat
from igor.diskfree import Diskfree
from igor.nodetoolstatus import Nodetoolstatus
from igor.elasticpost import Elasticpost
from multiprocessing import Process

ehosts = ['172.20.128.6']

class processClass:

    def __init__(self):
        p = Process(target=self.run, args=())
        p.daemon = True                       # Daemonize it
        p.start()                             # Start the execution

    def run(self):
         # This might take several minutes to complete
         while True:
            ns=Nodetoolstatus()
            rbody = ns.get()
            epost = Elasticpost()
            result = epost.post(['172.20.128.6'], 'cassandra', 'igor', json.dumps(rbody))
            time.sleep(2)


INTERVAL = 30 # seconds
APP = Flask(__name__)
API = Api(APP)

API.add_resource(Diskfree, '/diskfree')
API.add_resource(Nodetoolstatus, '/nodetoolstatus')
API.add_resource(Memstat, '/memstat')

@APP.route('/start', methods=['GET'])
def runit():
    try:
        begin = processClass()
    except:
        abort(500)
    return "Task is in progress"



if __name__ == '__main__':
    APP.run(debug=True)