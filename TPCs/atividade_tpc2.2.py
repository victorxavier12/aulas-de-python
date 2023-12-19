
nomes = ['victor', 'rogerio', 'bernardo']
notas = [20 , 15 , 18]

def addAluno():
    ddnome = input('\ndigite o nome que quer inserir: ')
    nomes.append(ddnome)
    ddnotas = input('adicione uma nota: ')
    notas.append(ddnotas)
    print('\n')

def modAlunoNome():
    modname = int(input('\ndigite o numero do aluno que quer editar o nome: '))
    nomemod = input('digite o novo nome do aluno: ')
    nomes[modname - 1] = nomemod
    print('\n')


def modNota():
    modnota = int(input('\ndigite o numero do aluno que quer editar a nota: '))
    notamod = int(input('digite a nova nota do aluno: '))
    notas[modnota - 1] = notamod
    print('\n')
    
naluno = len(nomes)
n = 0
m = 1

print ('\n########   BEM VINDO  ########\n')
print (f'nossa escola tem {naluno} alunos, eis a lista a baixo:\n')

while True:
    for nome in nomes:
        print(f'{m} - {nome}, com nota: {notas[n]}')
        n +=  1
        m += 1
    opcao = int(input('\ndigete uma opção sendo (1) - adicionar um novo alno; (2) - modificar nome do aluno; (3) - modificar nota: '))
    if opcao == 1:
        addAluno()
    elif opcao == 2:
        modAlunoNome()
    elif opcao == 3:
        modNota()
    else:
        print('\n>>>OPÇÃO INVALIDA<<<\n')
    n = 0
    m = 1


