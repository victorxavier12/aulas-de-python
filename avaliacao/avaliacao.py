import funcoesfc as fc

fc.criarficheiro()
#fc.addusuario()
def buscar_usuario(login,senha):
    usuarios = []
    try:
        with open('avaliacao/credenciais.txt', 'r+' , encoding='utf-8') as credenciais:
            for linha in credenciais:
                linha = linha.strip(',')
                usuarios.append(linha.split())
            for usuario in usuarios:
                nome = usuario[0]
                password = usuario[1]
                if login == nome and senha == password:
                    return True
    except FileNotFoundError:
        return False

login = input('digite nome de usuario: ')
senha = input('digite senha: ')

user = buscar_usuario(login,senha)

if user == True:
    print('login com sucesso')
    while True:
        print('opções:')
        print('(1) adicionar novo usuario:')
        print('(2) - encerrar:')
        opcao = int(input('digite sua opção: '))
        if opcao == 1:
            fc.addusuario()
        elif opcao == 2:
            break
        else:
            print('opção invalida')
else:
    print('login errado')
        


    
