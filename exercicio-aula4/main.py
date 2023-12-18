import calculadora 

while True:
    a = int(input('digite um numero:'))
    b = int(input('digite  outro umero:'))
    escolha = int(input('escolha um calcaco sendo (1)=soma; (2)=divisão; (3)=multiplicaçõa; (4)=subtração:'))
    if escolha == 1:
       calculadora.soma(a , b)
       break
    elif escolha == 2:
        calculadora.div(a , b)
        break
    elif escolha == 3:
        calculadora.mult(a , b)
        break
    elif escolha == 4:
        calculadora.sub(a , b)
        break
    else:
        print ('seleção de operação invalida')

