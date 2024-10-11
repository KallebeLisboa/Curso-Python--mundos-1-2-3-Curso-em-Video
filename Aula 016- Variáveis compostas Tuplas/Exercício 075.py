
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
n4= int(input('Digite outro número: '))

lista = [n1, n2, n3, n4]
count9 = 0
posicao3 = int()
par = int()


if n4 == 9:
    count9 += 1
elif n4 == 3:
    posicao3 = 3
elif n4 % 2 == 0:
    par += 1
if n3 == 9:
    count9 += 1
elif n3 % 2 == 0:
    par += 1
elif n3 == 3:
    posicao3 = 2
if n2 == 9:
    count9 += 1
elif n2 == 3:
    posicao3 =1
elif n2 % 2 == 0:
    par += 1
if n1 == 9:
    count9 += 1
elif n1 == 3:
    posicao3 = 0
elif n1% 2 == 0:
    par += 1



print(lista)

if count9 > 0:
    print(f'Na lista o 9 aparece {count9}')
else: 
    print('Não há o número 9 nessa lista')
if n1 or n2 or n3 or n4 == 3:
    print(f'O número 3 apareceu na posição {posicao3}')
else:
    print('Não há número 3 nessa lista')
if n1 % 2 == 0 or n2 % 2 == 0 or n3 % 2 == 0 or n4 % 2 == 0:
    print(f'Nessa lista existem {par} números par. Os números são', end = " ")
    for n in lista:
        if n % 2 ==0:
             print(n, end = " ")
else:
    print('Não há numero par nessa lista')