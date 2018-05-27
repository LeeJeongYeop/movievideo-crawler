import requests
import json

from config import MOVIE_LIST_URL, POST_PARAM_LIST
from database_connector import save_movie_info_list

MAX_MOVIE_COUNT = 15

# 요청 함수
def get_html(url, param):
  reponse = requests.post(url, data=param)
  return reponse.text

# 데이터 수신
param = {'paramList': POST_PARAM_LIST}
response = json.loads(get_html(MOVIE_LIST_URL, param))

# 영화리스트 추가
movie_info_list = []
for data in response['Movies']['Items']:
  data['PosterURL']
  movie_title = data['MovieNameKR']
  if (data['MovieNameKR'] != 'AD'):
    movie_info_list.append({
      "movie_title": data['MovieNameKR'],
      "movie_poster_url": data['PosterURL']
    })
  if (len(movie_info_list) >= MAX_MOVIE_COUNT):
    break

# 영화리스트 DB저장
save_movie_info_list(movie_info_list)