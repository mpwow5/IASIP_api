# It's Always Sunny in Philadelphia API
An API showing information about episodes of It's Always Sunny in Philadelphia (TV series).
User can add information about series, update and delete them.

# POST method

Reques:
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
 

# GET method

Base URL - https://api-iasip.herokuapp.com/

Resource: /api/episodes/

Request parameters: episodes_id

Response:

Status 200. OK:

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
 
Status 404. This episode doesn't exist

{
    "message": "This episode doesn't exist"
	
}

# PUT method

Base URL - https://api-iasip.herokuapp.com/

Resource: /api/episodes/

Request parameters: episode_id

Body:
{"IMDB rating": 9.2, "director": "Richie Keen"},

Status 200. OK

{
	"message": "Episode successfuly updated"
}

Status 404. This episode doesn't exist

{
    "message": "This episode doesn't exist"
	
}


# DELETE method

Base URL - https://api-iasip.herokuapp.com/

Resource: /api/episodes/

Body: 
{
	"episode_id": 6
}

Status 200. OK

{
	"message": "Episode successfuly deleted"

Status 404. This episode doesn't exist

{
    "message": "This episode doesn't exist"
	
}

