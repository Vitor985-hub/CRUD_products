import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    INSERT INTO PRODUCTS (nome, preco, quantidade, categoria)
    VALUES (?, ?, ?, ?)
    ''', ('shampoo premium', 29.90, 10, 'higiene pessoal'))

conn.commit()
conn.close()

print('produto inserido com sucesso.')