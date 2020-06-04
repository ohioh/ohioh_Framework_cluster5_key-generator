from flask_restful import Resource
from flask_http_response import success, result, error
from main.tasks import test_task


class StatusView(Resource):
    
    def get(self):
        return success.return_response('Hi this is flask boilerplate', 200)
