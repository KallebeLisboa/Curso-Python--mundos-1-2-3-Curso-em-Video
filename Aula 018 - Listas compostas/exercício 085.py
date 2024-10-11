princ = [[], []]



for c in range (1, 8):
    n = int(input(f'Digite o {c}o valor: '))
    if n % 2 ==0:
        princ[0].append(n)
    else:
        princ[1].append(n)


print(f'Os valores pares digitados foram {princ[0]}')
print(f'Os valores ímpares digitados foram {princ[1]}')