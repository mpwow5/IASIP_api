from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

episodes = {
    1: {'test': 'test', 'test2': 'test'},
    2: {'test': 'test', 'test2': 'test'}
}

parser = reqparse.RequestParser()
parser.add_argument('test', type=str)
parser.add_argument('test2', type=str)


class Main(Resource):
    def get(self, episode_id):
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




api.add_resource(Main, '/api/episodes/<int:episode_id>')  # Добавляем обработку URL адреса в класс Main. В URL добавлен
# динамический параметр, который позволяет отслеживать конкретный эпизов

if __name__ == '__main__':
    app.run(debug=True, port=3000, host="127.0.0.1")
