"""
TODO: Name the App
"""
from flask import Flask
from flask_restful import Resource, Api
#import subprocess

from igor import diskfree as df
from igor import nodetoolstatus as nts

APP = Flask(__name__)
API = Api(APP)

class HelloWorld(Resource):
    """
    /
    """
    def get(self):
        """
        hello world
        """
        return {'hello': 'world'}

class Diskfree(Resource):
    """
    /diskfree
    """
    def get(self):
        """
        we should name this something other than dummy
        """
        result = df.main(Resource)
        return result

class NodeToolStatus(Resource):
    """
    /diskfree
    """
    def get(self):
        """
        we should name this something other than dummy
        """
        result = df.main(Resource)
        return result

class NodeToolStatus(Resource):
    """
    /nodetoolstatus
    """
    def get(self):
        """
        we should name this something other than dummy
        """
        result = nts.main(Resource)
        return result

API.add_resource(HelloWorld, '/')
API.add_resource(Diskfree, '/diskfree')
API.add_resource(NodeToolStatus, '/nodetoolstatus')

if __name__ == '__main__':
    APP.run(debug=True)
