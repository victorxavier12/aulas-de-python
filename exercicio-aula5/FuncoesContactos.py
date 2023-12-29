import os

def criarficheiro():
    if os.path.exists('exercicio-aula5/contatos.txt'):
        # print ('\nficheiro contatos existe')
        next
    else:
        with open('exercicio-aula5/contatos.txt', 'w' , encoding='utf-8') as contatos:
            # print('fichiro contatos criado')
            next

def addcontatos():
    with open('exercicio-aula5/contatos.txt', 'a', encoding='utf-8') as contatos:
        nome = input('dige o nome do contato: ')
        telemovel = int(input('digite o contacto telefonico: '))
        contatos.write(f'{nome} - {telemovel}\n')


def listarcontatos():
    with open('exercicio-aula5/contatos.txt', 'r', encoding='utf-8') as contatos:
        lista = contatos.readlines()
        if not lista:
            print('lista de contato vazia')
        else:
            print(lista)
        
def mostrarcontatos():
    if os.path.exists('exercicio-aula5/contatos.txt'):
        with open('exercicio-aula5/contatos.txt', 'r', encoding='utf-8') as contatos:
            for linha in contatos:
                nome, telemovel = linha.strip().split('-')
                print(f'nome : {nome}, telemovel : {telemovel}')