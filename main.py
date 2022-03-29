from flask_restful import Resource, reqparse
from episodes_list import episodes

parser = reqparse.RequestParser()
parser.add_argument('test', type=str)
parser.add_argument('test2', type=str)


class Main(Resource):
    def get(self, episode_id=0):
        if episode_id == 0:
            return episodes
        else:
            return episodes[episode_id]

    def delete(self, episode_id):
        del episodes[episode_id]
        return episodes

    def post(self, episode_id):
        episodes[episode_id] = parser.parse_args()
        return episodes

    '''/api/episodes/3, {'test': 'test', 'test2': 'test'}'''

    def put(self, episode_id):
        episodes[episode_id] = parser.parse_args()
        return episodes

    '''/api/episodes/3, {'test': 'test', 'test2': 'test'}'''
