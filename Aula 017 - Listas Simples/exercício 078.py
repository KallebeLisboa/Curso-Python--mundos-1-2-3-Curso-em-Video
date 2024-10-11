num = []
maior = 0
menor = 0

for count in range (0,5):
    num.append(int(input(f'Digite um valor para posição {count}: ')))
    if count == 0:
        maior = menor = num[count]
    else:
        if num[count] > maior:
            maior = num[count]
        if num[count] < menor:
            menor = num[count]
print (f'O maior número é {maior} e está na posição ', end = '') 
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...\n', end = '')

print(f'O menor número é {menor} e está na posição ', end = '' )
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end = '')
print()