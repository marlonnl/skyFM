import os
import requests
import dotenv

dotenv.load_dotenv()

PERIODS = {
	0: "overall",
	7: "7day",
	30: "1month",
	90: "3month",
	120: "6month",
	360: "12month"
}

def get_data(username: str, period_: int, grid: list) -> dict: 
	"""
	Retrieves a JSON fro mthe last.fm API
	returns a dictionary as the following format:
		topalbums
			album
				{id}
					artist
						url
						name
						mbid
					image
						0 / 1 / 2 / 3
					mbid
					url
					playcount
					@attr
					name
	"""

	period = PERIODS[period_]
	total_albums = grid[0] * grid[1]
	headers = { "user-agent": username }
	params = {
		"api_key": os.getenv("LASTFM_API_KEY"),
		"user": username,
		"method": "user.gettopalbums",
		"period": period,
		"format": "json",
		"limit": total_albums
	}

	# API Request
	r = requests.get("https://ws.audioscrobbler.com/2.0/", headers=headers, params=params)
	print("encoding: ", r.encoding)
	# print("text: ", r.text)
	raw_data = r.json()

	# print("json data: ", raw_data)

