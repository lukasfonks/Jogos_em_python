def jogar():

    import random

    print('***************************')
    print('******Jogo da Forca!*******')
    print('***************************')

    arquivo = open('lista_frutas.txt', 'r')
    lista_de_palavras = []

    for linha in arquivo:
        linha = linha.strip()
        lista_de_palavras.append(linha)
    arquivo.close()

    index_palavra_secreta = random.randrange(0, len(lista_de_palavras))

    palavra_secreta = lista_de_palavras[index_palavra_secreta].upper()

    acertos = ['_' for letra in palavra_secreta]

    print(acertos)
    enforcou = False
    completou_palavra = False
    chances = 6

    while '_' in acertos and chances != 0:

        chute = input('Digite seu chute:')
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    acertos[index] = letra
                index += 1
            print(acertos)
        elif chute not in palavra_secreta:
            print('Você errou. A letra _{}_ não possui'.format(chute))
            chances = chances - 1
            if chances != 0:
                print('Você tem {} chances'.format(chances))

    if '_' not in acertos and chances != 0:
        print('Parabéns, você venceu!! A palavra secreta é {}'.format(palavra_secreta))
    else:
        print('Que pena, você nao conseguiu dessa vez. A palavra secreta era {}'.format(palavra_secreta))
    print('Fim do Jogo!')

if __name__ == '__main__':
    jogar()