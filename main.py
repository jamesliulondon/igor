from flask import Flask
from flask_restful import Resource, Api
import subprocess

from igor import cassandra as dummy

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Cassandra(Resource):
    def get(self):
        result=dummy.main(Resource)
        return result




api.add_resource(HelloWorld, '/')
api.add_resource(Cassandra, '/cassandra')

if __name__ == '__main__':
    app.run(debug=True)
