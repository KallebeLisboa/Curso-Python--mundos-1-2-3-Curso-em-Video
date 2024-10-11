# Pergunte a um funcionário seu salário. Se for > q 1250, aumento de 10%, se for menor aumento de 15%#

salario = float(input('Qual é seu salário? '))

if salario >= 1250.0:
    aumento = salario*1.1 
    print(f'seu salário é de {salario}R$, com o aumento seu salário atual passou a ser {aumento}R$')
else:
    aumento = salario*1.15
    print(f'seu salário é de {salario}R$, com o aumento seu salário atual passou a ser {aumento}R$')