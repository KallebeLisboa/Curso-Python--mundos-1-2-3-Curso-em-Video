import random



lista = list()
listapar = list()
print('-'*30)

def sortear(lista):
    """
    Utilizado para sortear números aleatorios
    """
    for c in range(0,5):
        x = random.randint(1,10)
        lista.append(x)
    print(f'A lista dos números sorteados é {lista}')

sortear(lista)
print('-'*30)
def somapar(lista):
    for valor in lista:
        if valor % 2 == 0:
            listapar.append(valor)
    if len(listapar) == 0:
        print(f'Não foram sorteados nenhum número par, e a soma entre eles é {sum(listapar)}')
    else:
        print(f'A lista dos números par é {listapar}, e a soma entre eles é {sum(listapar)}')

somapar(lista)
print('-'*30)

help(print)