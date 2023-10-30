def jogar():

    import random

    print('*******************************')
    print('*****Jogo de Adivinhação*******')
    print('*******************************')

    numero_secreto = random.randint(0,20)

    numero_tentativas = 4

    chute = int(input('Digite o seu chute de 0 a 20:'))

    print('Você digitou o número: {}'.format(chute))

    while chute != numero_secreto and numero_tentativas > 0:
        numero_tentativas -= 1
        if chute > numero_secreto and numero_tentativas > 0:
            print('Seu chute foi maior do que o número secreto. Você tem {} tentativas'.format(numero_tentativas))
            chute = int(input('Digite o novo chute:'))

        elif chute < numero_secreto and numero_tentativas > 0:
            print('Seu chute foi menor do que o número secreto.Você tem {} tentativas'.format(numero_tentativas))
            chute = int(input('Digite o novo chute:'))


    if chute == numero_secreto:
        print('Parabéns, você acertou o número secreto!!')

    elif chute != numero_secreto and numero_tentativas == 0:
        print('Você esgotou suas chances. O número secreto era {}'.format(numero_secreto))

if __name__ == '__main__':
    jogar()