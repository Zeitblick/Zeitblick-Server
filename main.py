from flask import Flask
from flask_restful import Resource, Api, reqparse
from environment import env_config
import os
import MySQLdb

app = Flask(__name__)
api = Api(app)

# Connect with MySQL
env = os.getenv('SERVER_SOFTWARE')
if (env and env.startswith('Google App Engine/')):
  # Connecting from App Engine
  db = MySQLdb.connect(
    unix_socket=env_config['MYSQL_SOCKET_PATH'],
    user=env_config['MYSQL_USER'])
else:
  # Connecting from an external network.
  # Make sure your network is whitelisted
  db = MySQLdb.connect(
    host=env_config['MYSQL_IP'],
    port=3306,
    user=env_config['MYSQL_USER'],
    passwd=env_config['MYSQL_PASSWORD'])
cursor = db.cursor()
cursor.execute('SELECT 1 + 1')

# Config REST API
@app.route('/')
def hello_world():
    return 'Hello World, %s' % env_config['MYSQL_DATABASE']

class SimilarHeadRotation(Resource):
    def post(self):
        try:
        # return {'inventory_no': result[1]}
            return {'result': 'works'}
        except Exception as e:
            return {'error': str(e)}

api.add_resource(SimilarHeadRotation, '/SimilarHeadRotation')

if __name__ == '__main__':
    app.run()
