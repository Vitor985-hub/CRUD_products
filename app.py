from flask import Flask, request, jsonify
from crud import *

app = Flask(__name__)

# create
@app.route('/products', methods=['POST'])
def criar_product():
    data = request.json

    create_product(
        data['nome'],
        data['preco'],
        data['quantidade'],
        data['categoria']
    )

    return jsonify({'message': 'produto adicionado com sucesso!'}), 201

#read

@app.route('/products', methods=['GET'])
def listar_produtos():
    produtos = list_produtos()

    resultado = []
    for p in produtos:
        resultado.append({
            'id': p[0],
            'nome': p[1],
            'preco': p[2],
            'quantidade': p[3],
            'categoria': p[4],
            'data_criacao': p[5]
        })

    return jsonify(resultado), 200

# update and delete

@app.route('/products/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def produto_por_id(id):

    if request.method == 'GET':
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM PRODUCTS WHERE id = ?', (id,))
        product = cursor.fetchone()
        conn.close()

        if product is None:
            return jsonify({'error': 'produto não encontrado'}), 404
        
        return jsonify({
            'id': product[0],
            'nome': product[1],
            'preco': product[2],
            'quantidade': product[3],
            'categoria': product[4],
            'data_criacao': product[5]
        }), 200
    
    elif request.method == 'PUT':
        data = request.json

        update_product(
            id,
            data.get('nome'),
            data.get('preco'),
            data.get('quantidade'),
            data.get('categoria')
        )

        return jsonify({'message': 'produto atualizado com sucesso!'}), 200

    elif request.method == 'DELETE':
        delete_product(id)
        return jsonify({'message': 'produto deletado com sucesso!'}), 200


if __name__ == '__main__':
    app.run(debug=True)