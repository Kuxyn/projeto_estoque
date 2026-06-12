import json

def salvar_dados(estoque):
#FUNÇÃO RESPONSÁVEL POR SALVAR OS DADOS NO ESTOQUE
    with open("estoque.json", "w", encoding="utf-8") as arquivo:
        json.dump(estoque, arquivo, indent=4, ensure_ascii=False)

def carregar_dados():
#FUNÇÃO RESPONSÁVEL POR CARREGAR OS DADOS VINDOS DO ARQUIVO JSON
    try:
        with open("estoque.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
            return []