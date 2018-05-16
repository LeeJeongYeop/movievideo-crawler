import requests
import json
from datetime import datetime

import config
from database_connector import get_movie_list

# 당일 영화 리스트 호출
today = datetime.today().strftime('%Y-%m-%d')
movie_list = get_movie_list(today)

# 영화별 youtube 영상 호출
for movie in movie_list:
  params = {
  "key" : config.YOUTUBE_SERVICE_KEY,
  "part": "id",
  "q": movie['title'],
  "type": "video",
  "maxResults": 10
  }
  response = requests.get(config.YOUTUBE_SEARCH_URL, params=params)
  print(len(json.loads(response.text)['items']))

# TODO:영화별 영상 리스트 저장