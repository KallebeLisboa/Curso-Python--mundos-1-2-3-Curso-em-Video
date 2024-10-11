#Leia a idade de 7 pessoas e indique quantas pessoas são maiores e menores#
import datetime

maior = 0
menor = 0
for pess in range(1, 8):
    nascimento = int(input(f'Digite a data de nascimento da pessoa número {pess}: '))
    idade = datetime.date.today().year - nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Temos {maior} pessoas maiores de idade e {menor} menores de idade')