import funcoesfc as fc

fc.criarficheiro()
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
         
while True:
    v = input('digite nome de usuario: ')
    s = input('digite senha: ')

    user = buscar_usuario(v,s)

    if user == True:
        print('login com sucesso')
        while True:
            print('opções:')
            print('(1) adicionar novo usuario:')
            print('(2) - fazer login')
            print('(3) - encerrar')
            opcao = int(input('digite sua opção: '))
            if opcao == 1:
                fc.addusuario()
            elif opcao == 2:
                break
            elif opcao == 3:
                break
            else:
                print('opção invalida')
    else:
        print('login errado')
    
    if opcao == 3:
        break