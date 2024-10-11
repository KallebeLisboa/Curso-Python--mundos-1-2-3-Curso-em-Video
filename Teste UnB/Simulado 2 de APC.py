# Questão 1


# Questão 2

def contagem_progressiva(numero):
    if numero == -10:
        print(numero)  # Caso base: quando chega a -10, imprime o número
    else:
        contagem_progressiva(numero - 1)  # Chamada recursiva, diminuindo o número em 1
        print(numero)  # Após a chamada recursiva, imprime o número atual

# Questão 3

n = int(input())  # Número de itens na lista de Seu Januário
lista_januario = {}  # Dicionário para armazenar os itens da lista de Seu Januário

# Lê os itens e os armazena no dicionário lista_januario
for i in range(n):
    produto, quantidade = input().split()
    quantidade = float(quantidade)  # Converte a quantidade para número decimal
    lista_januario[produto] = quantidade

m = int(input())  # Número de itens no catálogo da feira
catalogo_feira = {}  # Dicionário para armazenar os itens do catálogo da feira

# Lê os itens e seus preços, armazenando no dicionário catalogo_feira
for i in range(m):
    produto, preco_unitario = input().split()
    preco_unitario = float(preco_unitario)  # Converte o preço para número decimal
    catalogo_feira[produto] = preco_unitario

valor_total = 0  # Variável para acumular o valor total da compra

# Verifica se os itens da lista de Seu Januário estão no catálogo da feira
for produto in lista_januario.keys(): # .keys() retorna todas as chaves (nomes dos produtos) do dicionário
    if produto in catalogo_feira.keys(): # Verifica se o produto de Seu Januário está nas chaves do catálogo da feira
        valor_total += catalogo_feira[produto] * lista_januario[produto]  # Calcula o custo do item
    else:
        print(f'{produto} esta em falta')  # Imprime caso o item esteja em falta

print(f'{valor_total:.2f}')  # Imprime o valor total formatado com duas casas decimais

