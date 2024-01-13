import random

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "jogo", "desenvolvimento"]
    return random.choice(palavras)

def exibir_palavra_oculta(palavra, letras_corretas):
    resultado = ""
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra
        else:
            resultado += "_"
    return resultado

def jogar_forca():
    palavra_secreta = escolher_palavra().lower()
    letras_corretas = set()
    tentativas_maximas = 6
    tentativas = 0

    print("Bem-vindo ao Jogo da Forca!")
    
    while tentativas < tentativas_maximas:
        palavra_oculta = exibir_palavra_oculta(palavra_secreta, letras_corretas)
        print("\nPalavra: " + palavra_oculta)

        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas:
            print("Você já tentou essa letra. Tente novamente.")
            continue

        if letra in palavra_secreta:
            letras_corretas.add(letra)
            print("Letra correta!")
        else:
            print("Letra incorreta. Tente novamente.")
            tentativas += 1

        if set(palavra_secreta) == letras_corretas:
            print("\nParabéns! Você acertou a palavra: " + palavra_secreta)
            break

        if tentativas == tentativas_maximas:
            print("\nGame over! A palavra era: " + palavra_secreta)

if __name__ == "__main__":
    jogar_forca()