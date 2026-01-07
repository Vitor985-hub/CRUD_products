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

# update
@app.route('/products/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    data = request.json

    update_product(
        id,
        data.get('nome'),
        data.get('preco'),
        data.get('quantidade'),
        data.get('categoria')
    )

    return jsonify({'message': 'produto atualizado com sucesso!'}), 200

# delete
@app.route('/products/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    delete_product(id)
    return jsonify({'message': 'produto deletado com sucesso'}), 200

if __name__ == '__main__':
    app.run(debug=True)