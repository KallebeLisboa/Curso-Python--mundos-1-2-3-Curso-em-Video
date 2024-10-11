
def ficha(nome = '<desconhecido>', gols = 0):
    nome = str(input('Nome do jogador: '))
    gols = input('Número de gols: ')
    if nome == '' and gols == '':
        return(f'O jogador <desconhecido> fez 0 gols no campeonato 00')
    elif nome == '':
        return(f'O jogador <desconhecido> fez {gols} gols no campeonato')
    elif gols == '':
        return(f'O jogador {nome} fez 0 gols no campeonato')
  
print(ficha())