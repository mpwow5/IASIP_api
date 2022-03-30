from flask import Flask
from flask_restful import Api
from main import Main


app = Flask(__name__)
api = Api(app)


api.add_resource(Main, '/api/episodes/')


if __name__ == '__main__':
    app.run(debug=True, port=3000, host="127.0.0.1")
