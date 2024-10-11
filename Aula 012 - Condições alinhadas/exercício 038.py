# Leia dois númeors inteiros e compare-os
# O primeiro valor é maior / o segundo valor é maior / N existe valor maior, ambos iguais #

n1 = float(input('Ecolha um número: '))
n2 = float(input('Escolha outro número: '))

if n1 > n2:
    print(f'O primeiro valor "{n1}" é maior que o segundo "{n2}"')
elif n1 < n2:
    print(f'O segundo valor "{n2}" é maior que o primeiro "{n1}"')
else:
    print(f'Não há valor maior, ambos são iguais "{n1}" e "{n2}"')