import funcoesdex as fc
import json

fc.criarFicheiro()

while True:
            print('opções:')
            print('(1) - adicionar novo produto:')
            print('(2) - mostrar lista')
            print('(3) - editar quantidade')
            print('(3) - deletar um item')
            opcao = int(input('digite sua opção: '))
            if opcao == 1:
                fc.addjson()
            elif opcao == 2:
                fc.listaritens()
            elif opcao == 3:
                break
            else:
                print('opção invalida')
fc.addjson()