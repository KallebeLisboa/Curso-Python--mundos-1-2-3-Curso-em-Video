num = []
continuar = 'S'
newnumber = 0
escolha = 'S', 's', 'N', 'N'

while continuar == 'S':
    n =int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado')
    else:
        print('Valor repetido')
    continuar = str(input('Deseja continuar [S/N]? ')).upper()
    print('-='*30)
    while continuar not in escolha:
        continuar = str(input('Digite S parta continuar ou N para Parar [S/N]? ')).upper()
print(sorted(num))