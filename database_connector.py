import pymysql
from datetime import datetime

import config
from sqls import MOVIE_INSERT_SQL, MOVIE_LIST_SQL, LATELY_MOVIE_CRAWL_DATA, VIDEO_INSERT_SQL

def get_conn():
  return pymysql.connect(
    host=config.HOST,
    user=config.USER,
    password=config.PASSWORD,
    db=config.DATABASE,
    charset=config.CHARSET)

# 영화 정보 리스트 저장
def save_movie_info_list(movie_info_list):
  conn = get_conn()
  cursor = conn.cursor(pymysql.cursors.DictCursor)
  today = datetime.today().strftime('%Y-%m-%d')
  for movie_info in movie_info_list:
    if movie_info['movie_title'] == '':
      continue
    cursor.execute(MOVIE_INSERT_SQL, (movie_info['movie_title'], movie_info['movie_poster_url'], today))
  conn.commit()
  conn.close()

# 영화 목록
def get_movie_list(today):
  conn = get_conn()
  cursor = conn.cursor(pymysql.cursors.DictCursor)
  cursor.execute(MOVIE_LIST_SQL, (today))
  conn.commit()
  conn.close()
  return cursor.fetchall()

# 최근 영화 크롤링 날짜
def get_lately_movie_crawl_date():
  conn = get_conn()
  cursor = conn.cursor(pymysql.cursors.DictCursor)
  cursor.execute(LATELY_MOVIE_CRAWL_DATA)
  conn.commit()
  conn.close()
  return str(cursor.fetchone()['lately_date'])

# 영상 정보 리스트 저장
def save_video_info_list(video_info_list):
  conn = get_conn()
  cursor = conn.cursor(pymysql.cursors.DictCursor)
  for video_info in video_info_list:
    movie_title = video_info['movie_title']
    for video_data in video_info['movie_video_list']:
      try:
        cursor.execute(VIDEO_INSERT_SQL, (
          movie_title,
          video_data['video_id'],
          video_data['video_title'],
          video_data['video_description'],
          video_data['video_cover_image_url'],
          video_data['video_published_date']
          ))
        conn.commit()
      except Exception:
        print("[{} - {}] 인코딩에 맞지 않는 문자를 포함한 영상입니다.".format(movie_title, video_data['video_id']))
  conn.close()