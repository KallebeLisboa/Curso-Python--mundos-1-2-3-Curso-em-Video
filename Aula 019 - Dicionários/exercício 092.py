import datetime

dados = dict()

dados['nome'] = str(input('Nome: '))
dados['nasc'] = int(input('Data de nascimento: '))
dados['carteira'] = int(input('Digite o número da carteira de trabalho [0 n tem]: '))

idade = (datetime.datetime.now().year) - dados['nasc']
dados['idade'] = idade

if dados['carteira'] != 0:
    dados['contratacao'] = int(input('Digite o ano de contratação: '))
    dados['salário'] = float(input('Digite o salário: '))
    dados['aposentadoria'] = (dados['contratacao'] + 35) - dados['nasc']

print('-='*15)

for k, v in dados.items():
    print(f'    - O {k} é {v}')
print('-='*15)
