import FuncoesContactos as fc # as fc cria uma abreviação das funcoes de contatos

fc.criarficheiro()
print('\n#### BEM VINDO ####')
utilizador = input('\ndigite seu nome: ')
print(f'\nseção iniciada por : {utilizador}')



while True:
    
    a = int(input('\nselecione as seguintes opções (1) - adicionar contado; (2) -  mostrar lista: '))
    if a == 1:
        fc.addcontatos()
    elif a == 2:
        fc.listarcontatos()
    elif a == 3:
        fc.mostrarcontatos()
    else:
        print('\nessa opção nao existe')