from flask_restful import Resource, Api

class Memstat(Resource):
    def get(self):
        return "hello world"