brasileirão = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print('\n{:=^30}'.format(' BRASILEIRÃO 2020c '))
print('''\nEscolha uma das opções abaixo para exibir:
[ A ] Os 5 primeiros
[ B ] Os últimos 4 colocados
[ C ] Times em ordem alfabética
[ D ] Em que posição o Chapecoense
[ E ] Sair''')
while True:
    opcao = str(input('Digite a opção desejada: ')).upper().strip()
    if opcao == 'A':
        for c in (brasileirão[0:5]):
            print(c)
    elif opcao == 'B':
        print(brasileirão[-4:])
    elif opcao == 'C':
        print(sorted(brasileirão))
    elif opcao == 'D':
        print('O Chapecoense entá em {}o.'.format(brasileirão.index('Chapecoense')+1))
    elif opcao == 'E':
        break