nomes = list()
dados = list()
continuar = ''
count = 0
pesada = 0
leve = 0

while True: 
    dados.append(str(input('Digite um nome: ')))
    dados.append(int(input('Digite um Peso em Kg: ')))
    print('-='*30)
    if len(nomes) == 0:
        pesada = leve = dados[1]
    else: 
        if dados[1] > pesada:
            pesada = dados[1]
        if dados[1] < leve: 
            leve = dados[1]
    nomes.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar [S/N]:')).upper()
    count += 1

    while continuar != 'S' and continuar!= 'N':
        continuar = str(input('Deseja continuar? Digite S para continuar ou N para Parar [S/N]:')).upper()
    if continuar == 'N':
        break


print(nomes)
print(f'Foram cadastradas {count} pessoas')
print(f'O maior peso foi {pesada} e o Menor foi {leve}')