# Calcule preço da viagem. o.50$ para até 200km e 0.45 acima disso#

d = int(input('Quantos Kms será a viagem: '))

if d <= 200: 
    v = d*0.5
    print(f'A distancia percorrida foi de {d}Km')
    print(f'O preço cobrado pela viagem será de {v}R$')
else:
    v = d*0.45
    print(f'A distancia percorrida foi de {d}Km')
    print(f'O preço cobrado pela viagem será de {v}R$')