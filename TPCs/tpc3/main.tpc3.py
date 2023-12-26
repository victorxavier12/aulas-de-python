import funcoesFilmes as ff


ff.criarficheiro()
print('\n####  BEM VINDO  ####\n')

while True:
    ff.menu()

    op = int(input('\ndigite o numero da opção:'))
    if op == 1:
        ff.addfilme()
    elif op == 2:
        ff.listarfilmes()
    elif op == 3:
        break
    else:
        print('\n opção invalida')


