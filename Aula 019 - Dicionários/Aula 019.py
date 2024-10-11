pessoas ={'nome': 'Kallebe', 'Sexo': 'M', 'Idade': 19 }

print(pessoas)
print(f'O {pessoas["nome"]} tem {pessoas["Idade"]} anos')

print('-='*30)

print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())

print('-='*30)

pessoas['Sexo'] = 'Masculino'
pessoas['Peso'] = 66

for k, v in pessoas.items():
    print(f'{k} = {v}')

print('-='*30)

brasil = []

estado = {'Uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'Uf': 'São Paulo', 'Sigla': 'SP'}

brasil.append(estado)
brasil.append(estado2)

print(brasil[0]['Uf'])

print('-='*30)

turma = list()
aluno = dict()

for c in range (0,3):
    aluno['nome'] = str(input('Digite o nome do aluno: '))
    aluno['idade'] = int(input('Digite a idade do aluno: '))
    turma.append(aluno.copy())
for e in turma:
    for k, v in e.items():
        print(f'O campo {k} tem elementos {v}')