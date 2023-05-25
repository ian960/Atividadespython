import random

temas_palavras = {
    'animais': ['gato', 'cachorro', 'elefante'],
    'frutas': ['banana', 'abacaxi', 'uva'],
    'países': ['brasil', 'canadá', 'japão'],
    'cores': ['azul', 'verde', 'amarelo'],
    'profissões': ['médico', 'engenheiro', 'professor']
}

def escolher_palavra(tema):
    palavras_tema = temas_palavras.get(tema)
    if palavras_tema:
        palavra = random.choice(palavras_tema)
        return palavra
    else:
        return None

def verificar_vitoria(palavra_secreta, letras_corretas):
    for letra in palavra_secreta:
        if letra not in letras_corretas:
            return False
    return True

def jogar_forca():
    print("Bem-vindo ao jogo da forca!")

    while True:
        tema = input("Escolha um tema (animais, frutas, países, cores, profissões): ")
        palavra_secreta = escolher_palavra(tema)
        if palavra_secreta:
            break
        print("Tema inválido. Escolha novamente.")

    letras_corretas = []
    letras_erradas = []
    tentativas = 5

    while True:
        print("\nTema: " + tema)
        print("Palavra: ", end="")

        for letra in palavra_secreta:
            if letra in letras_corretas:
                print(letra, end=" ")
            else:
                print("_", end=" ")

        print("\nLetras erradas: " + ", ".join(letras_erradas))
        print("Tentativas restantes: " + str(tentativas))

        if verificar_vitoria(palavra_secreta, letras_corretas):
            print("\nParabéns! Você acertou a palavra '" + palavra_secreta + "'. Você venceu!")
            break

        if tentativas == 0:
            print("\nGame over! A palavra era '" + palavra_secreta + "'. Você perdeu!")
            break

        letra_jogador = input("Digite uma letra: ").lower()

        if letra_jogador in letras_corretas or letra_jogador in letras_erradas:
            print("Você já jogou essa letra. Tente novamente.")
            continue

        if letra_jogador in palavra_secreta:
            letras_corretas.append(letra_jogador)
            print("Parabéns! A letra está na palavra.")
        else:
            letras_erradas.append(letra_jogador)
            tentativas -= 1
            print("Ops! A letra não está na palavra.")

jogar_forca()
