import random
computador=random.randint(0, 5)#Faz o computador sortear
jogador=int(input('Digite um valor: '))
if computador==jogador:
    print('Você acertou!')
else:
    print('Você errou! ')


