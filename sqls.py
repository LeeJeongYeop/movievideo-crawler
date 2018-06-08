# MOVIE
MOVIE_INSERT_SQL = """INSERT INTO movie(movie_title, poster_image_url, crawling_date) VALUES (%s, %s, %s)"""
MOVIE_LIST_SQL = """SELECT * FROM movie WHERE crawling_date = %s"""
LATELY_MOVIE_CRAWL_DATA = """SELECT MAX(crawling_date) lately_date FROM movie"""

# VIDEO
VIDEO_INSERT_SQL = """INSERT INTO video(movie_title, video_id, video_title, video_description, video_cover_image_url, video_published_date) VALUES (%s, %s, %s, %s, %s, %s)"""
VIDEO_ID_DISTINCT_LIST_SQL = """SELECT DISTINCT video_id FROM video WHERE movie_title = %s"""