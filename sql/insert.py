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




async def insert_product(data: dict):
    conn = sqlite3.connect('mars.db')
    cursor = conn.cursor()

    photo = data.get('photo')
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    chat_id = data.get('chat_id')
    query = (f"""insert into products ( price, name, photo, description, chat_id)
             values ({price}, '{name}','{photo}', '{description}', {chat_id})""")

    cursor.execute(query)
    conn.commit()
    return True
