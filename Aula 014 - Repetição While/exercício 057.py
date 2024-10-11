#Leia o Sexo e so Aceite M ou F. pessa novamente se tiver errado até vir certo #



sexo = str(input('Digite seu Sexo: ')).strip().upper()[0]

while sexo not in 'FfMm':
    sexo = str(input('Digite seu Sexo novamente: ')).strip().upper()[0]
print(f'Seu sexo é {sexo}')