import pymysql
from datetime import datetime

import config
from sqls import MOVIE_INSERT_SQL, MOVIE_LIST_SQL, LATELY_MOVIE_CRAWL_DATA

def get_conn():
  return pymysql.connect(
    host=config.HOST,
    user=config.USER,
    password=config.PASSWORD,
    db=config.DATABASE,
    charset=config.CHARSET)

# 영화 타이틀 저장
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