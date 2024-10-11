lista = []
continuar = ''

listaPar = []
listaImpar= []


while True:
    n = int(input('Escolha um número: '))
    lista.append(n)
    if n %2 == 0:
        listaPar.append(n)
    else:
        listaImpar.append(n)

    continuar = str(input('Deseja continuar [S/N]: ')).upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar. Digite S para continuar e N para parar [S/N]: ')).upper()
    if continuar == 'N':
        break

print(f'A lista completa é {lista}')
print(f'A lista dos númeors Par {listaPar}')
print(f'A lista do números ípares é {listaImpar}')