
import random

quantidade = 5
aleatorio = [random.randint(1,100) for _ in range(quantidade)]

lista = aleatorio

menor = 0

print(f'Os valores sorteados foram {lista}')
print(f'O maior valor é {max(lista)} e o menor {min(lista)}')
