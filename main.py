from flask import Flask
from flask_restful import Resource, Api, reqparse
app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello World, haha!'

class SimilarHeadRotation(Resource):
    def post(self):
        try:
        # return {'inventory_no': result[1]}
            return {'result': "holler"}
        except Exception as e:
            return {'error': str(e)}

api.add_resource(SimilarHeadRotation, '/SimilarHeadRotation')

if __name__ == '__main__':
    app.run()
