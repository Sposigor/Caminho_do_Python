num = int(input('Entre com um número de 0 a 9999: '))
n = str(num)

print('\nAnalizando o número {}'.format(n)) 
print('\nUnidade: {}'
    '\nDezena: {}'
    '\nCentena: {}'
    '\nMilhar: {}'
    .format(n[3], n[2], n[1], n[0]))