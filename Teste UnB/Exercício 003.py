
januario = list()
compras = dict()



print('Digite chega para encerrar a lista')
while True:
    compras['alimento'] = str(input('nome do alimento: '))
    compras['quantidade'] = int(input('Quantidade do item anterior: '))
    januario.append(compras.copy())
    continuar = str(input('Dejesa continuar: ')).upper().strip()
    if continuar == 'NÃO':
        break


print(januario)