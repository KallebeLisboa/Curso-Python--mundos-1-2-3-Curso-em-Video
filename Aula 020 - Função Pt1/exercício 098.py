from time import sleep

def contagem(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print("-"*51)
    print(f'  O número ínicial é {i}, o final é {f} e o pulo é {p}')
    print("-"*51)
    count = i

    if count < f:
        while count <= f:
            print(f'{count}', end = " ", flush=True)
            count += p
            sleep(0.3)
            
    else:
        count = i
        while count >= f:
             print(f'{count}', end = " ", flush=True)
             count -=p
             sleep(0.3)
    print()
    print('Fim')
contagem(1,10,1)

sleep(1)

contagem(10, 0, 2)

sleep(1)

print('Agora é a sua vez: ')

ini = int(input('Digite um número inicial: '))
fim = int(input('Digite um número final: '))
pas = int(input('Digite um número para ser o Pulo: '))

contagem(ini, fim, pas)