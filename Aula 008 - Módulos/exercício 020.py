# O professor do desafio anterior quer sortar a ordem de
# apresentação de trabalhos dos alunos. Faça o nome dos quatro
# alunos e motre sua ordem sorteada #

import random

n1 = input('Nome do aluno: ')
n2 = input('Nome do aluno: ')
n3 = input('Nome do aluno: ')
n4 = input('Nome do aluno: ')
lista = [n1, n2, n3, n4]

random.shuffle(lista)

print(f'A ordem dos grupos são \n{lista}')