import random

def jogar(): #atenção nos itens 3 e 4, como usamos eles em outros segmentos tivemos que tornalos
    #variaveis
    #1
    mensagem_abertura()

    #2
    palavra_secreta = definindo_palavras()

    #3
    letras_acertadas = escondendo_letras(palavra_secreta)

    print(letras_acertadas)



    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        print("jogando")

        # 4
        chute=pede_chute()

        if (chute in palavra_secreta):
            #5
            revelando_letras(palavra_secreta, chute, letras_acertadas)

        else:
            erros = erros + 1
            desenha_forca(erros)

        enforcou = erros == 7

        acertou = "_" not in letras_acertadas # aqui definimos que se não houver mais _ o cara ganha
        print(letras_acertadas)



        if acertou:
            #6
            mensagem_vitoria(palavra_secreta)

        if enforcou:
            #7
            mensagem_derrota(palavra_secreta)

    print("Fim do jogo")



#1
def mensagem_abertura():
    print("***********Welcome***********")
    print("Bem vindo ao jogo da forca!")

#2
def definindo_palavras():
    arquivo = open("palavras.txt", "r")
    lista_de_palavras = []
    for linha in arquivo:
        linha = linha.strip()
        lista_de_palavras.append(linha)

    arquivo.close()

    print(lista_de_palavras)

    numero = random.randrange(0, len(lista_de_palavras))

    palavra_secreta = lista_de_palavras[numero].upper()
    return palavra_secreta

#3
def escondendo_letras(palavra_secreta):
    letras_acertadas = ["_" for letra in palavra_secreta]
    return letras_acertadas

#4
def pede_chute():
    chute = input("chute uma letra: ")
    chute = chute.strip().upper()
    return chute

#5
def revelando_letras(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra

        index = index + 1

#6
def mensagem_vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

#7
def mensagem_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

#8
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if (__name__ == "__main__"):
    jogar()

