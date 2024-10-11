matriz = [[0,0,0], [0,0,0], [0,0,0]]
par = 0
maior = 0
soma3coluna = 0


for m in range(0,3):
    for c in range(0,3):
        matriz[m] [c] = int(input(f'Digite um valor para a posição {m},{c}: '))
        if matriz [m] [c] % 2 == 0:
            par += matriz [m] [c]
print('-='*30)
for m in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[m] [c]:^5}]', end = '')
    print()
print('-'*30)
for m in range(0,3):
    soma3coluna += matriz [m] [2]
for m in range (0, 3):
    if c == 0:
        maior = matriz [1] [c]
    elif matriz [1] [c] > maior:
        maior = matriz[1] [c]

print(f'A soma dos números pares é {par}')
print(f'A soma dos números da terceira coluna é {soma3coluna}')
print(f'O maior número da segunda linha é {maior}')

