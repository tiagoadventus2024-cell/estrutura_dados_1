import json
from produto import Produto


def salvar(produtos):

    dados = []

    for produto in produtos:
        dados.append(produto.to_dict())

    with open("produtos.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)


def carregar():

    try:

        with open("produtos.json", "r", encoding="utf-8") as arquivo:

            dados = json.load(arquivo)

            produtos = []

            for item in dados:

                produtos.append(
                    Produto(
                        item["codigo"],
                        item["nome"],
                        item["categoria"],
                        item["preco"],
                        item["quantidade"]
                    )
                )

            return produtos

    except FileNotFoundError:
        return []
