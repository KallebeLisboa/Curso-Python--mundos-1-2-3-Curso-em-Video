

def voto(idade):
    idade = int(input('Digite sua data de nascimento: '))
    import datetime
    nasc = (datetime.datetime.now().year) - idade

    if nasc > 70:
        print('Seu voto é OPICIONAL')
    elif 16 <= nasc <= 17:
            print('Seu voto é OPICIONAL')
    elif nasc < 16:
         print('seu voto foi NEGADO')
    else:
         print('Seu Voto é OBRIGATÓRIO')
print('-'*30)

voto(idade = 0)
