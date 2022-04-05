from flask_restful import Resource, abort
from episodes_list import episodes
from flask import request


class Main(Resource):

    def get(self):
        episode_id = request.args.get('episode_id', type=int)
        print(episode_id)
        if episode_id == 0:
            return episodes
        elif episode_id not in episodes.keys():
            abort(404, message="This episode doesn't exist")
        else:
            return episodes[episode_id]

    def delete(self):
        episode_id = request.json['episode_id']
        if episode_id not in episodes.keys():
            abort(404, message="This episode doesn't exist")
        else:
            del episodes[episode_id]
            return {"message": "Episode successfuly deleted"}

    def post(self):
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            json = request.json
            episode_id = json['episode_id']
            episodes[episode_id] = json
            return {"status": "Episode added", "episode_id": episode_id}
        else:
            abort(415, message="Unsupported Media Type")

    def put(self):
        episode_id = request.args.get('episode_id', type=int)
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            if episode_id not in episodes.keys():
                abort(404, message="This episode doesn't exist")
            else:
                json = request.json

                for key in json:
                    for key2 in episodes[episode_id]:
                        if key == key2:
                            episodes[episode_id][key2] = json[key]
                return {"message": "Episode successfuly updated"}
        else:
            abort(415, message="Unsupported Media Type")
