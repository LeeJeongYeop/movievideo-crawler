import requests
import json
import re
from datetime import datetime

from config import YOUTUBE_SERVICE_KEY, YOUTUBE_SEARCH_URL
from database_connector import get_movie_list, save_video_info_list

MAX_VIDEO_COUNT = 10
VIDOE_PUBLISHED_DATE_FORMAT_INDEX = 10

# 당일 영화 리스트 호출
today = datetime.today().strftime('%Y-%m-%d')
movie_list = get_movie_list(today)

# 영화별 youtube 영상 호출 및 데이터셋 생성
video_info_list = []
for movie in movie_list:
  params = {
    "key": YOUTUBE_SERVICE_KEY,
    "part": 'snippet',
    "q": movie['movie_title'],
    "type": 'video',
    "maxResults": MAX_VIDEO_COUNT
  }
  response = requests.get(YOUTUBE_SEARCH_URL, params=params)
  video_list = {
    "movie_title": movie['movie_title'],
    "movie_video_list": []
  }
  for video_data in json.loads(response.text)['items']:
    video_list['movie_video_list'].append({
      "video_id": video_data['id']['videoId'],
      "video_title": video_data['snippet']['title'],
      "video_description": video_data['snippet']['description'],
      "video_cover_image_url": video_data['snippet']['thumbnails']['high']['url'],
      "video_published_date": video_data['snippet']['publishedAt'][:VIDOE_PUBLISHED_DATE_FORMAT_INDEX]
    })
  video_info_list.append(video_list)

# 영화별 영상 리스트 저장
save_video_info_list(video_info_list)