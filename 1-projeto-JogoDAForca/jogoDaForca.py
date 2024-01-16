import funcoesdeforca as fc

while True:
    fc.escolher_palavra() # chama a função que randomisa palavras 
    palavra_secreta = fc.escolher_palavra() # variavel que recebe a palavra e armazena
    letras_usuario = []
    letras_incorretas = []
    chanches = 6 
    print('####  JOGO DA FORCA  ####')
    while True:
        
        for i in palavra_secreta: # esse for ler letra por letra e verifica que se o usuario digitou uma letra corespondente e manten printado na tela 
            if i.lower() in letras_usuario:
                print(i, end=" ")
            else: 
                print('_', end=' ')
        print(f'voce tem {chanches} para adivinhar')
        print("\nletras incorretas usadas: ", end="")
        for i in letras_usuario:
            if i.lower() not in palavra_secreta:
                print( i , end=", ")

        letra = input("\n\nEscolha uma letra para adivinhar: ")
        letras_usuario.append(letra.lower())
        if letra.lower() in palavra_secreta.lower():
            print("\nPARABENS ACERTOU UMA DAS LETRAS")
 
        if letra.lower() not in palavra_secreta.lower():
            chanches -= 1
            print("\n!!!!voce errou a letra!!!!")

        ganhou = True
        for i in palavra_secreta:
            if i.lower() not in letras_usuario:
                ganhou = False
        
        if chanches == 0 or ganhou == True:
            break

    if chanches == 0:
        print(f"\n!!!!voce perdeu a palavra era : {palavra_secreta.upper()} !!!!\n")
    elif ganhou == True:
        print(f"\n!!!!PARABENS VOCE GANHOU A PALAVRA ERA : {palavra_secreta.upper()} !!!!\n")
    while True:
        print('DEJEJA TENTAR NOVAMENTE?\n')
        novojogo = input("(1) -  SIM / (2) - NÃO\n")
        if novojogo == "1":
            break
        elif novojogo == "2":
            break
        else:
            print("invalida selecione uma alternativa valida\n")
    if novojogo == "2":
        break