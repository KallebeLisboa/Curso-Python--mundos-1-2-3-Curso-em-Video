# contagem regressiva de 10 a 0 com tempo de 1 segundo entre eles#

import time

time.sleep(1)

start = input('Aperte Enter para iniciar o lançamento dos foguetes')

for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
print('BOOOOM!!')