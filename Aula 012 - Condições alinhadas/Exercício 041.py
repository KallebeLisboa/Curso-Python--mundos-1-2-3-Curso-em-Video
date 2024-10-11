# Leia uma idade de um atleta e classifique
# até 9 anos:Mirim/ 14: infantil/ 19: Júnior/  20: Sênior/ Acima: master #

import datetime

nascimento = int(input('Em qual ano você nasceu: '))
data = datetime.date.today().year

idade = data - nascimento

if idade <= 9:
    print(f'Sua idade é {idade}.Você é da categoria Mirim')
elif 9 < idade <= 14:
    print(f'Sua idade é {idade}.Você é da categoria infantil')
elif 14 < idade <= 19:
    print(f'Sua idade é {idade}. Você é da categoria Júnior')
elif idade == 20:
    print(f'Sua idade é {idade}. Você é da categoria Sênior')
else:
    print(f'Sua idade é {idade}. Você é da categoria Master')