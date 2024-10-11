lanche = ('hambúrguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('='*30)
print(len(lanche))
print('='*30)
for count in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[count]}')
print('=-'*30)
print(sorted(lanche))
print('='*30)
a = (2, 5, 4)
b = (1, 6, 7, 9, 5)
c= a + b

print(c)
print(len(c))
print(c.count(5))
print(c.index(9))


print('=-'*30)