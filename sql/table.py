import sqlite3


conn = sqlite3.connect('mars.db')
cursor = conn.cursor()

query = """
create table products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
photo TEXT,
name TEXT,
description TEXT,
price INTEGER,
chat_id INTEGER
)
"""

# query = """
# create table users(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT,
# phone_number INTEGER,
# modme_id INTEGER,
# modme_pass INTEGER,
# chat_id INTEGER
# )
# """

conn.commit()
cursor.execute(query)

