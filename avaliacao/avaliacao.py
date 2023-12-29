import funcoesfc as fc

fc.criarficheiro()
#fc.addusuario()


vfusu = input('digite nome de usuario: ')
vfsn = input('digite senha: ')

if vfusu and vfsn in fc.lista:
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


    
