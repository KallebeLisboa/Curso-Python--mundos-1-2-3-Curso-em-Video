n1 = float(input('Digite um número: '))
s = 0
count = 0

while True:
    s += n1
    count += 1
    n1 = float(input('Digite outro número: '))
    if n1 == 999:
        break
print(f'Foram digitados {count} valores. A soma dos númeors é {s}')