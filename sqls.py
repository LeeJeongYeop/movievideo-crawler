MOVIE_INSERT_SQL = """INSERT INTO movie(title, crawling_date) VALUES (%s, %s)"""
MOVIE_LIST_SQL = """SELECT * FROM movie WHERE crawling_date = %s"""