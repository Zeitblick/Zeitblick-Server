from flask import Flask
from flask_restful import Resource, Api, reqparse
from environment import env_config
import os
import MySQLdb

app = Flask(__name__)
api = Api(app)

def connectDB():
    env = os.getenv('SERVER_SOFTWARE')
    if (env and env.startswith('Google App Engine/')):
        # Connecting from App Engine
        db = MySQLdb.connect(
            unix_socket=env_config['MYSQL_SOCKET_PATH'],
            user=env_config['MYSQL_USER'],
            passwd=env_config['MYSQL_PASSWORD'])
    else:
        # Connecting from an external network.
        # Make sure your network is whitelisted
        db = MySQLdb.connect(
            host=env_config['MYSQL_IP'],
            port=3306,
            user=env_config['MYSQL_USER'],
            passwd=env_config['MYSQL_PASSWORD'])
    return db


# Config REST API
@app.route('/')
def hello_world():
    return 'Hello World, %s' % env_config['MYSQL_DATABASE']

class SimilarHeadRotation(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('pan', type=float, help='Left/Right rotation of head')
            parser.add_argument('tilt', type=float, help='Up/Down rotation of head')
            parser.add_argument('roll', type=float, help='Leaning of head')
            args = parser.parse_args()

            _pan = args['pan']
            _tilt = args['tilt']
            _roll = args['roll']

            pan_tolerance = 3.0
            tilt_tolerance = 3.0
            roll_tolerance = 10.0

            # query
            conn = connectDB()
            cursor = conn.cursor()

            cursor.execute('SELECT * FROM zeitblick_db.Faces WHERE panAngle < %s AND panAngle > %s AND '
                                                                 'tiltAngle < %s AND tiltAngle > %s AND '
                                                                 'rollAngle < %s AND rollAngle > %s',
                               (_pan + pan_tolerance, _pan - pan_tolerance,
                                _tilt + tilt_tolerance, _tilt - tilt_tolerance,
                                _roll + roll_tolerance, _roll - roll_tolerance,))

            result = cursor.fetchone()

            return {'inventory_no': result[1]}

        except Exception as e:
            return {'error': str(e)}, 500

        finally:
            cursor.close()
            conn.close()

api.add_resource(SimilarHeadRotation, '/SimilarHeadRotation')

if __name__ == '__main__':
    app.run()
