
def ficha():
    Nome = input('Nome do Jogador: ')
    if Nome == ' ' or Nome == '':
        Nome = '<Desconhecido>'
    Gol = input('Número de Gols: ')
    print(f'O jogador {Nome} fez {Gol} no campeonato!!')

ficha()