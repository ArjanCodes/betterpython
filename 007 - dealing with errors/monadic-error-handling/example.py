import sqlite3
from returns.result import Result, safe
from returns.pipeline import flow
from returns.pointfree import bind

class SQLite():
    def __init__(self, file='application.db'):
        self.file = file
        self.conn = None
    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        return self.conn.cursor()
    def __exit__(self, type, value, traceback):
        if self.conn: self.conn.close()
    
class NotFoundError(Exception):
    pass

class NotAuthorizedError(Exception):
    pass

def fetch_blog(blog_id) -> Result['Blog', Exception]:
    return flow(
        blog_id,
        fetch_blog_from_db,
        bind(blog_to_dict),
        bind(verify_access)
    )

@safe
def fetch_blog_from_db(blog_id):
    """Fetches blog from SQLite3 database."""
    with SQLite('application.db') as cur:
        cur.execute(f"SELECT * FROM blogs where id=?", [blog_id])
        result = cur.fetchone()
        if result is None:
            raise NotFoundError(f'Unable to find blog with id {blog_id}.')
        return result

@safe
def blog_to_dict(item) -> 'Blog':
    """Convert SQLite result to dictionary."""
    return { 
        'id': item[0],
        'published': item[1],
        'title': item[2],
        'content': item[3],
        'public': bool(item[4])
         }

@safe
def verify_access(blog) -> 'Blog':
    """Check that blog is accessible."""
    blog_id = blog['id']
    blog_public = blog['public']
    if not blog_public:
        raise NotAuthorizedError(f'You are not allowed to access blog with id {blog_id}.')
    return blog

res = fetch_blog("first-blog")
print(res)