import sqlite3

def connect_db():
    return sqlite3.connect('database.db')

def create_product(nome, preco, quantidade, categoria):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO PRODUCTS (nome, preco, quantidade, categoria)
        VALUES (?, ?, ?, ?)
        ''', (nome, preco, quantidade, categoria))
    
    conn.commit()
    conn.close()
    
def list_produtos():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM PRODUCTS')
    produtos = cursor.fetchall()

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

    sql = f"UPDATE PRODUCTS SET {', '.join(fields)} WHERE id = ?"
    cursor.execute(sql, values)
    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM PRODUCTS WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()