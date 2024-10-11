import random
from time import sleep

print('-'*30)
titulo = ('Jogar na mega sena'.upper())
print(f'{titulo:^30}')
print('-'*30)

jogos = int(input('Quantos jogos você deseja sortear? '))
frase = (f'Sorteando {jogos} jogos')
print('-='*3, frase, '-='*3)


for j in range (1, jogos+1):
    sorteio = list()
    sleep(0.5)
    for num in range (0, 6):
        n = int(random.randint(1,60))
        if n in sorteio:
            n = int(random.randint(1,60))
        else:
            sorteio.append(n)
    print(f'Jogo {j}: {sorteio}')
print('-='*4, 'Bom jogo', '-='*4)

