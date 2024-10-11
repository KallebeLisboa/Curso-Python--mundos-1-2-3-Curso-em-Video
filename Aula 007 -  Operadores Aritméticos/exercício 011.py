#Leia a altura e largura de uma parede e recaba a área
# e quantos L de tinta precisa para pintá-la (2m2 por l)


n1 = float(input('Largura da parede: '))
n2= float(input('Altura da parede: '))

a = n1*n2
t = a/2

print(f'A área da parede é {a}m2 e quantidade de tinta para pintá-la é {t:.2f}l')