matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for m in range (0, 3):
    for c in range (0,3):
        matriz[m] [c] = (int(input(f'Digite um valor para a posição {m},{c}: ')))
print(f'[{matriz[0][0]:^5}] [{matriz[0][1]:^5}] [{matriz[0][2]:^5}]')
print(f'[{matriz[1][0]:^5}] [{matriz[1][1]:^5}] [{matriz[1][2]:^5}]')
print(f'[{matriz[2][0]:^5}] [{matriz[2][1]:^5}] [{matriz[2][2]:^5}]')