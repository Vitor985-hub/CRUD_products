from crud import *

create_product('condicionador', 36.90, 12, 'higiene pessoal')

produtos = list_produtos()
for p in produtos:
    print(p)

update_product(1, preco=34.90, quantidade=15)
delete_product(2)
print("Produto deletado com sucesso.")