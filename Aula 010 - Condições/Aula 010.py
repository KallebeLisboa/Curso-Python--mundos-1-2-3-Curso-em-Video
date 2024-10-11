#idade = int(input('Qual sua idade? '))
#if idade >= 18:
#    print('Você é maior de idade!')
#else:
#    print('Você é menor de idade!') 

n1 = float(input('Nota primeiro bimestre: '))
n2 = float(input('Nota segundo semestre: '))
m = (n1+n2) / 2

if m >= 6.0:
    print(f'Sua média foi {m}. Aprovado!')
else:
    print(f'Sua média foi {m}. Reprovado!')