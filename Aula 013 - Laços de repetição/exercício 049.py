# Refaça o exercício 9, fazer a tabuada que o usuário escolher mas usando o Laço FOR#

n = int(input('Escolha um número: '))
n2 = n
for c in range(1, 11):
   print (f'{n} X {c} = {n*c}')