import sqlite3
import praw
import datetime
import time

reddit = praw.Reddit('bot1')
conn = sqlite3.connect('reddit_data.db')

with conn:

    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS reddit_comments
                  (date_time DATETIME,
                  subreddit VARCHAR(500),
                  title VARCHAR(500),
                  body VARCHAR(2000),
                  author VARCHAR(500)
                  )
                  """)

sqlFormula = "INSERT INTO reddit_comments (date_time, subreddit, title, body, author) VALUES (?, ?, ?, ?, ?)"

while True:
    try:
        subreddit = reddit.subreddit("wallstreetbets")
        for comment in subreddit.stream.comments(skip_existing=True):
            current_time = datetime.datetime.now()
            subreddit = str(comment.subreddit)
            author = str(comment.author)
            title = str(comment.link_title)
            body = str(comment.body)
            if len(body) < 2000:
                body = body
            elif len(body) > 2000:
                body = "data is too large" # extremely uncommon
            db = (current_time,subreddit,title,body,author)
            with conn:
                cursor = conn.cursor()
                cursor.execute(sqlFormula,db)
    except Exception as e:
        print(str(e))
        time.sleep(10)