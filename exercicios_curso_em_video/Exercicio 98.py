from time import sleep

def contagemAuto():
    print('~' * 25)
    print('Contagem de 1 até 10 de 1 em 1')
    for i in range(1, 11, 1):
        print(i, flush=True, end='  ')
        sleep(0.45)

    print('\n', '~' * 25)

    print('Contagem de 10 até 0 de 2 em 2')
    for x in range(10, -2, -2):
        print(x, flush=True, end='  ')
        sleep(0.45)

    print('\n', '~' * 25)

    print('Agora é sua vez de personalizar a contagem!')
    Inicio = int(input('Inicio: '))
    Fim = int(input('Fim: '))
    Passo = int(input('Passo: '))

    print('~' * 25)

    for x in range(Inicio, Fim, Passo):
        print(x, flush=True, end='  ')
        sleep(0.45)

contagemAuto()