from produto import Produto
from estoque import *

while True:

    print("\n=== SISTEMA DE ESTOQUE ===")
    print("1 - Cadastrar Produto")
    print("2 - Buscar Produto")
    print("3 - Listar Produtos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        codigo = int(input("Código: "))
        nome = input("Nome: ")
        categoria = input("Categoria: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))

        produto = Produto(
            codigo,
            nome,
            categoria,
            preco,
            quantidade
        )

        cadastrar_produto(produto)

    elif opcao == "2":

        codigo = int(input("Digite o código: "))

        produto = buscar_por_codigo(codigo)

        if produto:
            print(produto.nome)
        else:
            print("Produto não encontrado.")

    elif opcao == "3":

        for produto in produtos:

            print(
                produto.codigo,
                produto.nome,
                produto.preco,
                produto.quantidade
            )

    elif opcao == "0":

        print("Sistema encerrado.")
        break
