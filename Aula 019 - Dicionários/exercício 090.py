
aluno = dict()

aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['média'] = int(input(f'Digite média de {aluno["nome"]}: '))

if aluno['média'] > 7:
    print(f'{aluno["nome"]} passou de ano')
else:
    print(f'{aluno["nome"]} Reprovou de ano')

for k, v in aluno.items():
    print(f'O {k} é igual a {v}')