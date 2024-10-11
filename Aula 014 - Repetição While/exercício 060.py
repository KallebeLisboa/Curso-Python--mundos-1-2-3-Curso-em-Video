#Escolha um número e mostre seu fatorial#

n1 = c = int(input('Escolha um número para fatorar: '))
f = 1

while c > 0:
    f *= c
    c -=1
print(f)