num = int(input('Digite um número para calcular o seu factorial: '))
cont = num
fat = 1
print(f'Calculando {num}! = ', end='')
for c in range(cont, 0, -1):
    print(c, end='')
    print(' X' if c > 1 else ' =', end=' ')
    fat *= c
print(fat)



