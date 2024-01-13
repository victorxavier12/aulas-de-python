import funcoesdeforca as fc


while True:
    fc.escolher_palavra() # chama a função que randomisa palavras 

    palavra_secreta = fc.escolher_palavra() # variavel que recebe a palavra e armazena

    letras_usuario = []
    chanches = 10 

    print('####  JOGO DA FORCA  ####')
    while True:
        
        for i in palavra_secreta: # esse for ler letra por letra e verifica que se o usuario digitou uma letra corespondente e manten printado na tela 
            if i.lower() in letras_usuario:
                print(i, end=" ")
            else: 
                print('_', end=' ')
        
        print(f'voce tem {chanches} para adivinhar')


        print(f"letras usadas: {letras_usuario}")

        letra = input("\nEscolha uma letra para adivinhar: ")
        letras_usuario.append(letra.lower())

        if letra.lower() not in palavra_secreta.lower():
            chanches -= 1


        ganhou = True
        for i in palavra_secreta:
            if i.lower() not in letras_usuario:
                ganhou = False
        
        if chanches == 0 or ganhou==True:
            break

    if chanches == 0:
        print(f"\n!!!!voce perdeu a palavra era : {palavra_secreta.upper()} !!!!\n")
    elif ganhou == True:
        print(f"\n!!!!PARABENS VOCE GANHOU A PALAVRA ERA : {palavra_secreta.upper()} !!!!\n")
    while True:
        print('DEJEJA TENTAR NOVAMENTE?\n')
        tentativa = input("(1) -  SIM / (2) - NÃO\n")
        if tentativa == "1":
            break
        elif tentativa == "2":
            break
        else:
            print("invalida selecione uma alternativa valida\n")
    if tentativa == "2":
        break

    
    
    