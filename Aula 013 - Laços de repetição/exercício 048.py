#Soma de todos os números ímpares e múltiplos de 3 de 1 a 500#

s = 0
cont = 0
for c in range(1,501, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print(f'A soma de todos os{cont} números é {s}')