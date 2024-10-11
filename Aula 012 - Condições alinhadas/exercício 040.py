
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2)/2

if media < 5.0:
    print(f'Sua média foi de {media}. Você está REPROVADO!')
elif 5.0 < media < 5.9:
    print(f'Sua média foi de {media}. Você está de RECUPERAÇÃO!')
else:
    print(f'Sua média foi de {media}. Você está APROVADO!')