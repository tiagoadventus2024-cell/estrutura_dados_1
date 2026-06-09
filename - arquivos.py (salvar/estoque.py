from produto import Produto

produtos = []

def cadastrar_produto(produto):

    for p in produtos:
        if p.codigo == produto.codigo:
            print("Código já existe.")
            return

    produtos.append(produto)
    produtos.sort(key=lambda x: x.codigo)

    print("Produto cadastrado com sucesso.")


def buscar_por_codigo(codigo):

    inicio = 0
    fim = len(produtos) - 1

    while inicio <= fim:

        meio = (inicio + fim) // 2

        if produtos[meio].codigo == codigo:
            return produtos[meio]

        elif codigo < produtos[meio].codigo:
            fim = meio - 1

        else:
            inicio = meio + 1

    return None


def buscar_por_nome(nome):

    encontrados = []

    for produto in produtos:
        if nome.lower() in produto.nome.lower():
            encontrados.append(produto)

    return encontrados


def remover_produto(codigo):

    produto = buscar_por_codigo(codigo)

    if produto:
        produtos.remove(produto)
        print("Produto removido.")
    else:
        print("Produto não encontrado.")
