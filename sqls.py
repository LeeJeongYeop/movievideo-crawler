MOVIE_INSERT_SQL = """INSERT INTO movie(title, poster_image_url, crawling_date) VALUES (%s, %s, %s)"""
MOVIE_LIST_SQL = """SELECT * FROM movie WHERE crawling_date = %s"""
LATELY_MOVIE_CRAWL_DATA = """SELECT MAX(crawling_date) lately_date FROM movie"""