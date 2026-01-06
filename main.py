from crud import *

def menu():
    print("=== menu de Produtos ===")
    print("1. Adicionar Produto")
    print("2. Listar Produtos")
    print("3. Atualizar Produto")
    print("4. Deletar Produto")
    print("5. Sair")

while True:
    menu()
    choice = input("Escolha uma opção: ")

    if choice == '1':
        nome = input('nome do produto: ')
        preco = float(input('preço do produto: '))
        quantidade = int(input('quantidade do produto: '))
        categoria = input('categoria do produto: ')

        create_product(nome, preco, quantidade, categoria)
        print('produto adicionado com sucesso!')

    elif choice == '2':
        produtos = list_produtos()
        print("=== Lista de Produtos ===")
        for p in produtos:
            print(p)

    elif choice == '3':
        product_id = int(input('ID do produto a ser atualizado: '))
        nome = input('novo nome (deixe em branco para não alterar): ')
        preco = input('novo preço (deixe em branco para não alterar): ')
        quantidade = input('nova quantidade (deixe em branco para não alterar): ')
        categoria = input('nova categoria (deixe em branco para não alterar): ')

        update_product(
            product_id,
            nome if nome else None,
            float(preco) if preco else None,
            int(quantidade) if quantidade else None,
            categoria if categoria else None
        )

        print('produto atualizado com sucesso!')

    elif choice == '4':
        product_id = int(input('ID do produto a ser deletado: '))
        delete_product(product_id)
        print('produto deletado com sucesso!')

    elif choice == '5':
        print('saindo...')
        break

    else:
        print('opção inválida, tente novamente.')