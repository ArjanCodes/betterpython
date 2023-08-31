import sqlite3

def blog_lst_to_json(item):
    return { 
        'id': item[0],
        'published': item[1],
        'title': item[2],
        'content': item[3],
        'public': bool(item[4])
         }

def fetch_blogs():
    pass

def fetch_blog(id: str):
    pass

