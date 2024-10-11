#leia o salário com um aumento

n1 = float(input('Qual seu salário atual? '))
n2 = float(input('Qual aumento será aplicado? '))

a = 1+(n2/100)
s = n1*a

print(f'Seu salário é de {n1}, com aumento de {n2} seu salário muda para {s}')