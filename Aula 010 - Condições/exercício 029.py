# Leia a velocidade de um carro, se ultrapassar 80km/h foi multado. A multa deve custar 7R$ por cada km acima da velocidade#

v = float(input('Qual foi a velocidade do carro em km? '))

m = (v - 80) * 7


if v > 80:
    print(f'Você foi multado em {m} Reais')
else:
    print('Você está dentro do limite de velocidade. boa viagem!')