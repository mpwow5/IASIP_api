# It's Always Sunny in Philadelphia API
An API showing information about top 5 episodes of It's Always Sunny in Philadelphia (TV series).
User can add information about series, update and delete them.

# Метод POST

Запрос:
Base URL - https://api-iasip.herokuapp.com/

Resource: /api/episodes/
Body:

{"episode_name": "The Gang Tries Desperately to Win an Award",
 "episode_id":6,
 "season": 9,
 "number in season": 3,
 "number overall": 96,
 "IMDB rating": 9.2,
 "director": "Richie Keen",
 "writers": ["David Hornsby"],
 "original air date": {"year": 2013, "month": "September", "day": 18},
 "storyline": "Once again, Paddys is passed up by the Philadelphia Free Press annual \"Best Bar In Philadelphia\" competition. So to win the award, the gang goes to the bar that did win the award in an attempt to stake out the competition."}
 

# Метод GET

Base URL - https://api-iasip.herokuapp.com/

Resource: /api/episodes/
Параметр для запроса: episodes_id

Ответ:

Статус 200. Успешный запрос
{"episode_name": "The Gang Tries Desperately to Win an Award",
 "episode_id":6,
 "season": 9,
 "number in season": 3,
 "number overall": 96,
 "IMDB rating": 9.2,
 "director": "Richie Keen",
 "writers": ["David Hornsby"],
 "original air date": {"year": 2013, "month": "September", "day": 18},
 "storyline": "Once again, Paddys is passed up by the Philadelphia Free Press annual \"Best Bar In Philadelphia\" competition. So to win the award, the gang goes to the bar that did win the award in an attempt to stake out the competition."}
 
Статус 404. Ошибка, данный эпизод отсутствует

{
    "message": "This episode doesn't exist"
	
}

# Метод PUT

Base URL - https://api-iasip.herokuapp.com/

Resource: /api/episodes/
Параметр для запроса: episode_id

Body:
{"IMDB rating": 9.2, "director": "Richie Keen"},

Статус 200. Успешный запрос

{
	"message": "Episode successfuly updated"
}

Статус 404. Ошибка, данный эпизод отсутствует

{
    "message": "This episode doesn't exist"
	
}


# Метод DELETE

Base URL - https://api-iasip.herokuapp.com/

Resource: /api/episodes/

В body передаем episode_id который необходимо удалить
{
	"episode_id": 6
}

Статус 200. Успешный запрос

{
	"message": "Episode successfuly deleted}

Статус 404. Ошибка, данный эпизод отсутствует

{
    "message": "This episode doesn't exist"
	
}

