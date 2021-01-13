from math import factorial

def fatorial(x, show=False):
    x_fact = factorial(x)
    print(f'O fatorial de {x} é {x_fact}.')

    if show:
        print('O cálculo desse fatorial é:')
        for c in range(x, 0, -1):
            print(f'{c}', end='')
            if c > 1:
                print(' . ',end='')
            else:
                print(' = ',end='')
        print(x_fact)
    else:
        print('Cálculo não exibido.')


x = int(input('Informe um número inteiro para o cálculo de seu fatorial: '))
fatorial(x, show=True)