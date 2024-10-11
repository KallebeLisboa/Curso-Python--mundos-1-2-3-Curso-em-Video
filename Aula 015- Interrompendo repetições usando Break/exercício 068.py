import random

v = 0
pc = random.randint(1, 10)
resultado = 0

while True:
    n1 = int(input('Escolha um número: '))
    escolha = str(input('Você quer par ou impar [P/I]: ')).strip().upper()[0]
    while escolha not in 'PpIi':
            escolha = str(input('Você quer par ou impar. Digite apenas P ou I [P/I]: '))
           
    resultado = pc + n1
    print('-'*20)
    if resultado % 2 == 0:
        resultado = 'Pp'
    else:
        resultado = 'Ii'
    if escolha in resultado:
        print(f'você ganhou! O pc escolheu {pc}')
    else:
        print(f'Você perdeu! O pc escolheu {pc}')
        break
    print('-'*20)
    v += 1
print(f'Você teve {v} vitórias conscutivas')