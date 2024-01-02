import os

def criarficheiro():
    if os.path.exists('avaliacao/credenciais.txt'):
        # print ('\nficheiro contatos existe')
        next
    else:
        with open('avaliacao/credenciais.txt', 'w' , encoding='utf-8') as credenciais:
            admin = 'victor'
            senhaadm = '180199'
            credenciais.write(f'{admin} {senhaadm}\n')
            # print('fichiro contatos criado')

def addusuario():
    with open('avaliacao/credenciais.txt', 'a' , encoding='utf-8') as credenciais:
        login = input('dige o usuario do contato: ')
        senha = input('digite o contacto telefonico: ')
        credenciais.write(f'{login} - {senha}\n')