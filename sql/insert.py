import sqlite3

async def insert_user(data: dict):
    conn = sqlite3.connect('mars.db')
    cursor = conn.cursor()

    chat_id = data.get('chat_id')
    name = data.get('name')
    phone_number = data.get('phone_number')
    modme_id = int(data.get('modme_id'))
    modme_pass = int(data.get('modme_pass'))

    query = f"""INSERT INTO users (name, phone_number, modme_id, modme_pass, chat_id)
             VALUES ('{name}', '{phone_number}', {modme_id}, {modme_pass}, {chat_id})"""

    cursor.execute(query)
    conn.commit()
    return True
