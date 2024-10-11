# Escreva um número e escolha sua P.A dos 10 primeiros#

n1 = int(input('Escolha um número inicial: '))
n2 = int(input('Escolha sua PA: '))
n3 = n1 + (10 - 1 )*n2
for c in range(n1, n3 + n2, n2):
    print(f'{c}', end = '-> ')
print('Acabou')