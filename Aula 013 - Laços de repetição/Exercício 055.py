#Leia o peso de 5 pessoas e informe o maior e o menor#


maior = 0
menor = 0

for peso in range (1, 6):
    p = float(input(f'Digite o peso da {peso}° pessoa: '))
    if peso == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        else:
            menor = p
print(f'O maior é {maior} e o menor é {menor}')