from random import randint
from time import sleep

def gerador(lista):
    print('Sorteando 5 valores da lista', end=' ')
    for cont in range(0, 10):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end=' ', flush=True)
        sleep(0.30)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somar dos valores pares é {soma}')

numeros = list()
gerador(numeros)
somaPar(numeros)