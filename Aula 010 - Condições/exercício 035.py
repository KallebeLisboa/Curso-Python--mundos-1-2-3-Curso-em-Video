#Leia três retas e diga se forma um triângulo #

n1 = float(input('Digite o lado de uma reta: '))
n2 = float(input('Digite o lado da outra reta: '))
n3 = float(input('Digite o lado da outra reta: '))

lista = [n1, n2, n3]
tudo = n1 + n2 + n3
medio = tudo - (min(lista) + max (lista)) 


if (min(lista) + medio) > max(lista):
    print('Parabéns, você possui um triângulo!')
else:
    print('infelizmente você não possui um triângulo!')