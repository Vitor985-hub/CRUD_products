import sqlite3

def connect_db():
    return sqlite3.connect('database.db')

def create_product(nome, preco, quantidade, categoria):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO produtos (nome, preco, quantidade, categoria)
        VALUES (?, ?, ?, ?)
        ''', (nome, preco, quantidade, categoria))
    
def list_produtos():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()

    for produto in produtos:
        print(produto)

    conn.close()
    return produtos

def update_product(product_id, nome=None, preco=None, quantidade=None, categoria=None):
    conn = connect_db()
    cursor = conn.cursor()

    fields = []
    values = []

    if nome is not None:
        fields.append("nome = ?")
        values.append(nome)
    if preco is not None:
        fields.append("preco = ?")
        values.append(preco)
    if quantidade is not None:
        fields.append("quantidade = ?")
        values.append(quantidade)
    if categoria is not None:
        fields.append("categoria = ?")
        values.append(categoria)

    values.append(product_id)

    sql = f"UPDATE produtos SET {', '.join(fields)} WHERE id = ?"
    cursor.execute(sql, values)
    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM produtos WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()