
def maior(*num):
    ma = 0
    me = 0
    
    if num == 0:
        print('Por favor digite um número')        
    else:
        print(f'Foram informados os numeros:', end = " ")
        for n in num:
            print(f' {n}', end = " ")
        print()
        print(f'Foram analisados {len(num)} valores e o maior é {max(num)}')
    


maior(1, 3, 4, 6, 2, 6, 7)