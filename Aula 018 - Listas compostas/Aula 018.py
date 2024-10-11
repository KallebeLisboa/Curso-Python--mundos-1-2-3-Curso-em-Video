teste = list()

teste.append('Kallebe')
teste.append(19)

galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(teste)
print(galera)
print('-='*30)
galera2 = [['joão', 29], ['Maria', 19], ['joca', 34]]

print(galera2[2][1])
print('-='*30)

for p in galera2:
    print(f'A idade do {p[0]} é {p[1]} ')
print('-='*30)

galera3 = list()
dados = list()
totmaior=0
totmenos=0
for c in range (0,3):
    dados.append(str(input('digite um nome: ')))
    dados.append(int(input('Digite uma idade: ')))
    print('-'*30)
    galera3.append(dados[:])
    dados.clear()
for idade in galera3:
    if idade[1] >= 21:
        print(f'{idade[0]} é maior de idade.')
        totmaior +=1
    else:
        print(f'{idade[0]} é Menor de idade.')
        totmenos+=1
print(f'Temos ao todo {totmaior} Maiores e {totmenos} Menores de idade')