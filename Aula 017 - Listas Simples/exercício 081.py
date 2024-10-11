lista = []
continuar = ''
count = 0

while True:
    print('-='*30)
    n = int(input('Digite um valor: '))
    continuar = str(input('Deseja continuar [S/N]')).upper()
    lista.append(n)
    count += 1
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Digite S para continuar ou N para parar [S/N]: ')).upper()
    else:
        if continuar != "S":
            break
print('-='*30)
print(f'Foram digitados {count} Valores!')
lista.sort(reverse=True)
print(f'A lista Digitada é {lista}')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('Número 5 não está na lista')