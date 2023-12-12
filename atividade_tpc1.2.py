idade = int(input('digite sua idade:'))
id = True

if idade >= 18 and id == True:
    print ('pode entrar no evento'),
elif idade < 18 and id == True:
    print ('nao tem idade para entrar')
else:
    print ('indentidade falsa')