jogadores = list()
jogador = dict()
from os import system
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).strip()
    jogador['gols'] = list()
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
    for c in range (0,jogador['partidas']):
        jogador['gols'].append(int(input(f'Quantos gols na partida {c+1} ? ')))
    jogador['total de gols'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    escolha = str(input('Deseja adicionar mais jogadores ? [Sim/Não] ')).strip().lower()[0]
    while escolha not in 'sn':
        print('ERRO! Por favor, digite uma opção válida ')
        escolha = str(input('Deseja adicionar mais jogadores ? [Sim/Não] ')).strip().lower()[0]
    if escolha == 'n':
        break
system('cls')
print(30*'=')
print(f'{"COD":<}{" NOME":<}{"GOLS":^17}{"TOTAL":>}')
print(30*'=')
for k, v in enumerate(jogadores):
    print(f' {k:<3}{v["nome"]:<9}{str(v["gols"]):<14}{v["total de gols"]}')
print(30*'=')
while True:
    aux = int(input('Digite o COD do jogador para ter uma visão geral (999 para encerrar): '))
    if aux == 999:
        break
    elif aux not in range(0,len(jogadores)):
        print('ERRO! COD não existente')
    else:
        print(f'Levantamento do jogador {jogadores[aux]["nome"]}:')
        for k, v in enumerate(jogadores[aux]['gols']):
            print(f' -No jogo {k+1} fez {v} gols')
system('cls')
print('PROGRAMA ENCERRADO')