
i = int(input('Escolha um número para iniciar: '))
f = int(input('Escolha um número para terminar: '))
p = int(input('Escolha um número para ir pulando: '))

s = 0
for c in range( i, f+1, p):
    print(c)
    s += c
print(f'o somatório foi {s}')
print('fim')