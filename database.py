import sqlite3

#conecta ou cria o banco de dados 
conn = sqlite3.connect('database.db')

# cursor para executar comandos sql
cursor = conn.cursor()

# criação da tabela

cursor.execute('''
CREATE TABLE IF NOT EXISTS PRODUCTS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL,
    categoria TEXT,
    data_criacao TEXT DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()
conn.close()

print("Banco de dados e tabela criadas com sucesso.")