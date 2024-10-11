# Leia um número e crie uma sequencia de fibonati mostrando o número de caracteres escolhido#

n1 = fim = int(input('Quantos elementos devem aparecer: '))
fib = 0
fib2 = 1

while fim > 0:
    fim -= 1
    print(f'{fib} -> {fib2}') 
print('Fim')
