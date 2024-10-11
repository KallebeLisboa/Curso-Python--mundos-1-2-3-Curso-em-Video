# Leia um ângulo qualquer e mostre na tela o valor do seno,
# Cosseno e tangente desse ângulo.

import math

an = float(input('Qual ângulo vc deseja: '))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))

print(f'O ângulo {an} possui o Seno {seno:.2}, Cosseno {cosseno:.2} e tangente {tangente:.2}')