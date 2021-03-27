import sqlite3

class SQLite():
    def __init__(self, file='application.db'):
        self.file=file
    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        return self.conn.cursor()
    def __exit__(self, type, value, traceback):
        print("Closing the connection")
        self.conn.close()

class NotFoundError(Exception):
    pass

class NotAuthorizedError(Exception):
    pass

def blog_lst_to_json(item):
    return { 
        'id': item[0],
        'published': item[1],
        'title': item[2],
        'content': item[3],
        'public': bool(item[4])
         }

def fetch_blogs():
    try:
        with SQLite('application.db') as cur:

            # execute the query
            cur.execute('SELECT * FROM blogs where public=1')

            # fetch the data and turn into a dict
            return list(map(blog_lst_to_json, cur.fetchall()))
    except Exception as e:
        print(e)
        return []

def fetch_blog(id: str):
    try:
        with SQLite('application.db') as cur:

            # execute the query and fetch the data
            cur.execute(f"SELECT * FROM blogs where id=?", [id])
            result = cur.fetchone()

            # return the result or raise an error
            if result is None:
                raise NotFoundError(f'Unable to find blog with id {id}.')
        
            data = blog_lst_to_json(result)
            if not data['public']:
                raise NotAuthorizedError(f'You are not allowed to access blog with id {id}.')
            return data
    except sqlite3.OperationalError:
        raise NotFoundError(f'Unable to find blog with id {id}.')
