
x = tuple(int(input('Digite o {}º numero: '.format(i+1))) for i in range(4))
print(x)
print(f'Quantidades de vezes que o 9 apareceu: {x.count(9)}')
while True:
    if 3 not in x:
        print('O número 3 não existe na tupla.')
        break
    else:
        print(f'Colocacão do número 3: {x.index(3) + 1}˚')
        break
print('Valores pares digitados:', end = " ")
for n in x:
    if n % 2 == 0:
        print(f'{n}', end = " ")