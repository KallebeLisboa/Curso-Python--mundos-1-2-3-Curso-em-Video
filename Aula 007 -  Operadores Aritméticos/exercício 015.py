#escreva um prgroama que pergunte o Km e dias do carro alugaado.
#Caucule o preço a paga. Sabendo que o carro custa 60$ dia e 0.15$km

d = float(input('Dias de uso do carro: '))
km = float(input('Kms rodados: '))

a = (d*60) + (km*0.15)

print(f'O aluguel do carro foi R${a}')