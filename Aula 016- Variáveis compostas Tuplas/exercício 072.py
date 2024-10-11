#cria uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte 
# Deverá ler um número pelo teclado entre 0 e 20 e mostrá-lo por extenso#

n1 = int(input('Digite um número no intervalo de 0 a 20: '))
num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessate', 'dezoito', 'dezenove', 'vinte' )

while  0 > n1 or n1 > 20: 
    n1 = int(input('o número deve estar entre intervalo de 0 a 20: '))
print(f'Você digitou no número {num[n1]} ')