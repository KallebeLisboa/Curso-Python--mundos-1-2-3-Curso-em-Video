
lista = list()
pessoa = dict()
mulheres = list()
continuar = ''
count = 0
media = 0

while True:
    pessoa['nome'] = str(input('Digite o nome: '))
    pessoa['idade'] = int(input('Digite a idade: '))
    pessoa['sexo'] = str(input('Qual o sexo da pessoa [M/F]: ')).upper().strip()
    count += 1
    media += pessoa['idade']

    while pessoa['sexo'] not in 'M, F':
        pessoa['sexo'] = str(input('Qual o sexo da pessoa. Digite M para masculino ou S para feminino [M/F]: ')).upper().strip()
    
    lista.append(pessoa.copy())

    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa.copy())

    continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()
    while continuar not in 'S, N':
        continuar = str(input('Deseja continuar. Digite S para sim e N para não [S/N]: ')).upper().strip()
    if continuar == 'N':
        break
print('-='*30)

resultado = media / count

print(f'Foram cadastradas {count} pessoas')
print(f'A média de idades é {resultado}')
if pessoa

print('As mulheres registradas são: ')
for c in range (len(mulheres)): 
    print(mulheres[c])
      