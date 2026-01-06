import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM products')
produtos = cursor.fetchall()

for produto in produtos:
    print(produto)

conn.close()