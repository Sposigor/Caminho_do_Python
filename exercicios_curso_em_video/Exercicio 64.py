cont = n = soma = 0

while n != 999:
    n = int(input('Digite um número: [999 para parar] '))
    if n != 999:
        soma += n
        cont += 1

print('No total, foram {} números digitados e a soma entre eles é {}.'.format(cont, soma))