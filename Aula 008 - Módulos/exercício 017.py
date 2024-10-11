#Leia o comprimento do cateto oposto e cateto adjacente de um
#triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math

cto = float(input('O tamanho do cateto oposto é: '))
cta = float(input('O tamanho do cateto Adjacente é: '))
hip2 = (cto**2) + (cta**2)
hip = math.sqrt(hip2)

print(f'A hipotenusa é {hip}')