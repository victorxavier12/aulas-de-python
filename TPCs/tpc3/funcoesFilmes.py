import os

def menu():
    print('MENU:\n')
    print('1 - adicionar filme')
    print('2 - mostrar lista de filmes')
    print('3 - encerrar programa')

def criarficheiro():
    if os.path.exists('TPCs/tpc3/filmes.txt'):
        next
    else:
        with open('TPCs/tpc3/filmes.txt', 'w', encoding='utf-8') as filmes:
            next

def addfilme():
    with open('TPCs/tpc3/filmes.txt', 'a', encoding='utf-8') as filmes:
        nomef = input('\ndige o nome do filme: ')
        filmes.write(f'- {nomef}\n')
        print()

def listarfilmes():
    with open('TPCs/tpc3/filmes.txt', 'r', encoding='utf-8') as filmes:
        lista = filmes.read()
        if not lista:
            print('\nlista de filmes vazia\n')
        else:
            print('\nlista de filmes:\n')
            print(lista)