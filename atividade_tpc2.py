

nomes = ['victor', 'rogerio', 'bernardo']
notas = [20 , 15 , 18]


def addAluno():
    ddnome = input('\ndigite o nome que quer inserir: ')
    nomes.insert(ddnome)
    ddnotas = input('adicione uma nota: ')
    notas.insert(ddnotas)

    
    
    


naluno = len(nomes)
n = 0
m = 1
print ('\n########   BEM VINDO  ########\n')
print (f'nossa escola tem {naluno} alunos, eis a lista a baixo:\n')
for nome in nomes:
    print(f'{m} - {nome}, com nota: {notas[n]}')
    n +=  1
    m += 1

addAluno()


for nome in nomes:
    print(f'{m} - {nome}, com nota: {notas[n]}')
    n +=  1
    m += 1