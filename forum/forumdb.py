# "Database code" for the DB Forum, connecting to real DB=Forum.

import datetime
import psycopg2, bleach

DBNAME = "forum"

POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
  
#old  """Return all posts from the 'database', most recent first."""
#old  return reversed(POSTS)

      db = psycopg2.connect(database=DBNAME)
      c  = db.cursor()
      c.execute("select content, time from posts order by time desc")
      posts = c.fetchall()
      db.close()

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  POSTS.append((content, datetime.datetime.now()))


