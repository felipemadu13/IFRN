info_produto = {}
produtos = []
seta = "-->"

def titulo(linhas, texto):
    print('=' * linhas)
    print(' ' * ((linhas - len(texto)) // 2) + texto)
    print('=' * linhas)

def calcular_total(valor, quantidade):
    return valor * quantidade

def imprimir_produtos(produtos):
    print("Nº   Produto          Valor   Qnt  Total")
    total_compras = 0
    for produto in produtos:
        total_compras += produto['total']
        print(f"{produto['numero']:<4} {produto['nome']:16} {produto['valor']:<4.2f} {produto['quantidade']: 5} {produto['total']:7.2f}")
    print(f"{seta:>34}", f"{total_compras:>5.2f}")

titulo(40, "Supermercado Tabajara")
def cadastro_produto():
    info_produto['nome'] = input(f"Produto {len(produtos) + 1}: ")
    info_produto['valor'] = float(input("Valor: "))
    info_produto['quantidade'] = int(input("Quantidade: "))
    info_produto['numero'] = len(produtos) + 1
    info_produto['total'] = calcular_total(info_produto['valor'], info_produto['quantidade'])
    produtos.append(info_produto.copy())

cadastro_produto()
while True:
    resposta = input("Quer inserir outro produto? S/N: ")
    if resposta.upper() == 'S':
        cadastro_produto()
    elif resposta.upper() == 'N':
        break
    else:
        print("Digite Novamente!")
        continue
    
titulo(40, "Confirmação e Exclusão")
while True:
    resposta = input("Quer retirar algum produto? S/N: ")
    if resposta.upper() == 'N':
        titulo(40, "Resumo das Compras")
        imprimir_produtos(produtos)
        break
    elif resposta.upper() == 'S':
        numero_produto = int(input("Qual o número do produto? "))
        encontrado = False
        for produto in produtos:
            if produto['numero'] == numero_produto:
                produtos.remove(produto)
                print(f"Item {produto['nome']} excluído!")
                encontrado = True
                break
        if encontrado == False:
            print("Item não encontrado!")
    else:
        print("Digite Novamente!")
