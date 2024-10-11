# Escreva um progrtama que faça o computador pensar entre o número de 0 a 5 e o usuário deverá tentar advinhar#

import random

lista = [0, 1, 2, 3, 4, 5]
escolha = random.choice(lista)

usuario = int(input('Escolha um número de 0 a 5: '))

if usuario == escolha:
    print (f'Parabéns, o número pensado pelo computador foi {escolha}, e o seu foi {usuario}. Você acertou !')
else:
    print(f'Infelizmente você errou. O número pensado pelo computador foi {escolha}, e o seu foi {usuario}. Você errou!')