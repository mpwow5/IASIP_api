from flask import Flask
from flask_restful import Api
from main import Main

app = Flask(__name__)
api = Api(app)

api.add_resource(Main, '/api/episodes/<int:episode_id>')
# Добавляем обработку URL адреса в класс Main. В URL добавлен
# динамический параметр, который позволяет отслеживать конкретный эпизов

if __name__ == '__main__':
    app.run(debug=True, port=3000, host="127.0.0.1")
