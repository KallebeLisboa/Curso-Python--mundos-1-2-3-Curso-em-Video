#num = [1, 2, 3, 4, 5]
#num[2] = 9
#num.append(7)
#num.sort(reverse=True)
#num.insert(2, 2)
#num.pop(2)
#num.remove(2)

#print(f'Essa lista possui {len(num)} Elementos')
#print(num)#

#-=-=-=-=-=-=-=-=-=-=-=-#

valores = []
for cont in range (0,5):
    valores.append(int(input('Digite um Valor: ')))
valores.sort()
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao fnal da lista.')