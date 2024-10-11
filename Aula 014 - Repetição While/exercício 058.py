#PC pensa em um número de 1 a 10. JOgador tenta acertar e enquento errar continua
# no final mostre as tentativas#

import random

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pc = random.choice(lista)
player = 1

jogo = int(input('Escolha um número de 1 a 10: '))

while jogo != pc:
    jogo = int(input('Você errou. Escolha um número novamente: '))
    player += 1 
print(f'Parabéns. Voce acertou! O número do Pc era {pc}.')
print(f'Foram precisas {player} tentativas até acertar')