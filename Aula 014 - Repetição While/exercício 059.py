#Crie um programa que leia 2 números na tela. Ele deve aparecer um menu
# [1] soma / [2] multiplicar/ [3] maior valor/ [4] novos números / [5] sair do programa#

n1 = float(input('Escolha um número: '))
n2 = float(input('Escolha outro número: '))


escolha = 0

while escolha != '5':
    print('-'*22)
    print('[1] Soma')
    print('[2] Multiplicar')
    print('[3] Mostrar maior valor')
    print('[4] Escolher novos números')
    print('[5] Encerrar programa')
    print('-'*22)
    escolha = str(input(''))
    print('-'*22)
    if escolha == '1':
        print(f'A soma é: {n1} + {n2} = {n1+n2}')
    if escolha == '2':
        print(f'A multiplicação é: {n1} X {n2} = {n1*n2}')
    if escolha == '3':
        if n1 > n2 :
            print(f'O maior número é {n1}')
        else:
            print(f'O maior valor é {n2}')
    if escolha == '4':
        n1 = float(input('Escolha um número novamente: '))
        n2 = float(input('Escolha outro número novamente: '))
print('Tenha um bom dia!')