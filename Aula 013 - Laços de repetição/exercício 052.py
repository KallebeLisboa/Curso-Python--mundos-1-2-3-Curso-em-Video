# LEia um número inteiro e diga se é primo ou não #

n1 = int(input('Digite um número: '))
tot = 0
for c in range(1, n1+1):
    if n1 % c == 0:
        print('\033[33m', end = ' ')
        tot += 1
    else:
        print('\033[31m', end = ' ')
    print(f'{c}', end = ' ')
print(f'\n\033[mO número {n1} foi divisivel {tot} Vezes')
if tot == 2:
    print('Esse número é primo')
else:
    print('Esse número não é primo')