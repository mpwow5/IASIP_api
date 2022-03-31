from flask_restful import Resource, abort
from episodes_list import episodes
from flask import request


class Main(Resource):
    """Метод GET. В запросе указываем параметр episodes_id.
    episodes_id = 0 возвращает список всех эпизодов.
    Если указан отсутствущий episode_id - возвращается информационное сообщение"""

    def get(self):
        episode_id = request.args.get('episode_id', type=int)
        print(episode_id)
        if episode_id == 0:
            return episodes
        elif episode_id not in episodes.keys():
            abort(404, message="This episode doesn't exist")
        else:
            return episodes[episode_id]

    """Метод удаляет указанный в параметрах запроса эпизод"""

    def delete(self):
        episode_id = request.json['episode_id']
        if episode_id not in episodes.keys():
            abort(404, message="This episode doesn't exist")
        else:
            del episodes[episode_id]
            return {"message": "Episode successfuly deleted"}

    """Метод позволяет добавлять эпизоды"""

    def post(self):
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            json = request.json
            episode_id = json['episode_id']
            episodes[episode_id] = json
            return episodes
        else:
            abort(415, message="Unsupported Media Type")

    """Изменяем описания уже добавленных эпизодов"""

    def put(self):
        episode_id = request.args.get('episode_id', type=int)
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            if episode_id not in episodes.keys():
                abort(404, message="This episode doesn't exist")
            else:
                json = request.json
                #  В переданных параметрах получаем json. Находим эпизод по episode_id и перебираем ключи в полученном
                #  json и сверяем с ключами в словаре эпизода. Если есть совпадения, перезаписываем
                #  старые значения значениями из полученного json
                for key in json:
                    for key2 in episodes[episode_id]:
                        if key == key2:
                            episodes[episode_id][key2] = json[key]
                return {"message": "Episode successfuly updated"}
        else:
            abort(415, message="Unsupported Media Type")
