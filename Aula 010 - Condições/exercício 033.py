#Escreva 3 números e diga qual é o menor, meio e maior#

n1 = int(input('Escolha um número: '))
n2 = int(input('Escolha outro número: '))
n3 = int(input('Escolha outro número: '))

lista = [n1, n2, n3]
tudo = n1 + n2 + n3
medio = tudo - (min(lista) + max (lista)) 

print(sorted(lista))

print(f'O número menor é {min(lista)}')
print(f'O número médio é {medio}')
print(f'O número maior é {max(lista)}')
