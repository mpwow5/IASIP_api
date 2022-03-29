from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('test', type=str)
parser.add_argument('test2', type=str)

episodes = {
    1: {'episode_name': 'Charlie Work',
        'season': 10,
        'number in season': 4,
        'number overall': 108,
        'IMDB rating': 	9.8,
        'director': 'Matt Shakman',
        'writers': ['Charlie Day', 'Glenn Howerton', 'Rob McElhenney'],
        'original air date': {'year': 2015, 'month': 'February', 'day': 4},
        'storyline': 'Charlie is determined to make sure Paddy\'s Pub passes its health inspection.'},
    2: {'episode_name': 'The Nightman Cometh',
        'season': 4,
        'number in season': 13,
        'number overall': 45,
        'IMDB rating': 9.7,
        'director': 'Matt Shakman',
        'writers': ['Charlie Day', 'Glenn Howerton', 'Rob McElhenney'],
        'original air date': {'year': 2008, 'month': 'November', 'day': 20},
        'storyline': 'Charlie stages a rock opera based on his song "Nightman," and recruits the rest of the gang to '
                     'help him with it.'},
    3: {'episode_name': 'The Gang Goes to a Water Park',
        'season': 12,
        'number in season': 2,
        'number overall': 126,
        'IMDB rating': 9.5,
        'director': 'Matt Shakman',
        'writers': ['Eric Ledgin'],
        'original air date': {'year': 2017, 'month': 'January', 'day': 11},
        'storyline': 'The gang takes a trip to a local waterpark, ripe with personal agendas and ulterior motives. '
                     'Dennis feeds off his mantra of "the park provides" and takes on a protégé. Frank and Charlie '
                     'are determined to ride every ride by any means necessary and Mac and Dee get stuck in a tube '
                     'slide for most of the day.'},


}



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
