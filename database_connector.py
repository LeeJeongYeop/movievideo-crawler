import pymysql
from datetime import datetime

import config
from sqls import MOVIE_INSERT_SQL

def get_conn():
  return pymysql.connect(
    host=config.HOST,
    user=config.USER,
    password=config.PASSWORD,
    db=config.DATABASE,
    charset=config.CHARSET)

# 영화 타이틀 저장
def save_movie_list(movie_list):
  conn = get_conn()
  cursor = conn.cursor(pymysql.cursors.DictCursor)
  today = datetime.today().strftime('%Y-%m-%d')
  for movie_title in movie_list:
    if movie_title == '':
      continue
    cursor.execute(MOVIE_INSERT_SQL, (movie_title, today))
  conn.commit()
  conn.close()