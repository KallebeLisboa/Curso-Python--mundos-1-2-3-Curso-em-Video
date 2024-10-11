#leia o preço de um produto e mostre seu novo preço com
#5% de desconto

n1 = float(input('Qual é o preço atual? '))
n2 = float(input('Qual desconto gostaria de aplicar? '))
d = 1-(n2/100)
p = n1*d

print (f'O preço atual é {n1}, com {n2}% de desconto fica {p}')