# Leia o ano de nascimento de um jovem. 
# se ainda vai se alistar/ Se vai / Se ja passou do tempo 
# Mostre o tempo que falta ou o prazo que passou #

import datetime

ano = int(input('Qual ano você nasceu: '))

data = datetime.date.today().year
idade = data - ano

ainda = 18 - idade
prazo = idade - 18

if idade < 18:
    print(f'Você não está na idade de se alistar. Volte em {ainda} anos!')
elif idade == 18:
    print(f'Parabéns, você está na idade correta para o alistamento.')
else:
    print(f'Infelizmente você já passou do prazo a {prazo} anos. Vá imediatamente para a junta de serviço militar mais próxima')