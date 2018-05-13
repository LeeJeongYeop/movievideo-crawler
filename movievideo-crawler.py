import requests
import json
import config

MOVIE_LIST_URL = config.MOVIE_LIST_URL
POST_PARAM_LIST = config.POST_PARAM_LIST

# 요청 함수
def get_html(url, param):
  reponse = requests.post(url, data=param)
  return reponse.text

# 데이터 수신
param = {'paramList': POST_PARAM_LIST}
response = json.loads(get_html(MOVIE_LIST_URL, param))

# 영화리스트 추가
movie_list = []
for data in response['Movies']['Items']:
  movie_name = data['MovieNameKR']
  if (movie_name != 'AD'):
    movie_list.append(movie_name)