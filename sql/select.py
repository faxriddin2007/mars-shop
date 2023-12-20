import sqlite3


async def get_user(chat_id: int):
    conn = sqlite3.connect('mars.db')
    cursor = conn.cursor()

    user = query = f'select * from users where chat_id={chat_id}'
    cursor.execute(query).fetchone()
    return user 
