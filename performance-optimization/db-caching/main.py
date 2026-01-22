from fastapi import FastAPI
from pydantic import BaseModel
import redis
import json
import hashlib
import sqlite3

app = FastAPI()
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def get_db_connection():
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn=get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    create table if not exists users(
                   id integer primary key,
                   name text not null,
                   age integer
                   )
""")
    
    cursor.execute("insert or ignore into users(id, name, age) values(1, 'John Doe', 45)")
    cursor.execute("insert  or ignore into users(id, name, age) values(2, 'Mike Tyson', 35)")
    cursor.execute("insert  or ignore into users(id, name, age) values(3, 'John Cena', 43)")
    conn.commit()
    conn.close()

init_db()

class UserQuery(BaseModel):
    user_id: int

def make_cache_key(user_id: int):
    raw=f"user:{user_id}"
    return hashlib.sha256(raw.encode()).hexdigest()

@app.post('/get-user')
def get_user(query: UserQuery):

    cache_key= make_cache_key(query.user_id)
    cached_data=redis_client.get(cache_key)

    if cached_data:
        print('serving from Redis Cache')
        return json.loads(cached_data)
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("select * from users where id=?", (query.user_id,))
    row=cursor.fetchone()
    conn.close()
    if row is None:
        return {'message': 'user not found!'}

    result={'id': row['id'], 'name': row['name'], 'age': row['age']}
    redis_client.setex(cache_key, 3600, json.dumps(result))
    print("Fetched from DB and cached") 
    return result