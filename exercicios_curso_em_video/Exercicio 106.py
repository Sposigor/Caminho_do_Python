def titulo(txt):
    print('\33[44;30m~'*(len(txt) + 4))
    print(f'\33[44;30;1m  {txt}  ')
    print('\33[44;30;1m~'*(len(txt) + 4))


def acesso(txt):
    print('\33[42;30m~'*(len(txt) + 36))
    print(f"\33[42;30;1m  Acessando o manual do comando '{txt}'  ")
    print('\33[42;30;1m~'*(len(txt) + 36))


def pyhelp():
    from time import sleep
    while True:
        titulo('SISTEMA DE AJUDA PyHELP')
        while True:
            try:
                fb = str(input('\33[mFunção ou Biblioteca > ')).strip()
                if not fb.isalpha():
                    print('Função ou biblioteca inválida.')
            except:
                print('Função ou biblioteca inválida.')
                continue
            if fb.isalpha():
                break
        if fb in 'FIMfim':
            break
        acesso(fb)
        sleep(1)
        print('\33[7;30m', end='')
        help(fb)


pyhelp()
titulo('Até Logo')