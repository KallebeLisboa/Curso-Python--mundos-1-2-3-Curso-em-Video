import moeda

num = int(input('Digite um número: '))
print(f'O dobro de R${num:.2f} é R${moeda.aumentar(num):.2f}')
print(f'A metade de R${num:.2f} é R${moeda.diminuir(num):.2f}')
