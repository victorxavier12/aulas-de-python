import json
import os

configuracoes = {
    "produto": "quantidade",
}

def criarFicheiro():
    if os.path.exists('exercicio-aula6/stock.txt'):
        # print ('\nficheiro contatos existe')
        next
    else:
        with open('exercicio-aula6/stock.txt', 'w' , encoding='utf-8', ) as stock:
            next

def addjson():
    with open('exercicio-aula6/stock.txt', 'a' , encoding='utf-8', ) as stock:
        produto = input('adicione um produto: ')
        verificar(produto)
        if verificar(produto) == True:
            print('\nproduto ja cadastrado\n')
        else:
            quantidade = int(input('adicione a quantidade: '))
            stock.write(f"{produto} , {quantidade}\n")
            print('\nproduto cadastado com sucesso!!')

def listaritens():
    with open('exercicio-aula6/stock.txt', 'r' , encoding='utf-8', ) as stock:
        lista = stock.readlines()
        if not lista:
            print('lista de contato vazia')
        else:
            print(lista)

def verificar(iten):
    produtos = []
    try:
        with open('exercicio-aula6/stock.txt', 'r' , encoding='utf-8', ) as stock:
            for linha in stock:
                linha = linha.strip(',')
                produtos.append(linha.split())
            for produto in produtos:
                nome = produto[0]
                if iten == nome:
                    return True  
    except FileNotFoundError:
        return False