# Emprestímo. Perguntar o valor da casa, salário do comprador, quantos anos ele vai pagar. 
# Caucule o valor da prestação mensal, n pode exceder 30% do salário ou o empréstimo será negado #

casa = float(input('Qual é o valor da casa: '))
salario = float(input('Qual é seu salário em R$: '))
tempo = int(input('Em quantos anos será paga a casa: '))

meses = tempo*12
prestaçao = casa/meses

if prestaçao > salario*0.30:
    print (f'Infelismente seu emprestimo foi negado.')
else:
    print (f'Parabéns, seu emprestimo foi aprovado')