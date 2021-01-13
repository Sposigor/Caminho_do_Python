matriz = [[], [], []]
somaPares = 0
somaColuna2 = 0
maior2 = 0
for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f'Digite o valor do elemento [{i},{j}]: '))
        matriz[i].append(n)
        if n % 2 == 0:
            somaPares += n
        if j == 2:
            somaColuna2 += n
        if i == 1:
            if j == 0 or n > maior2:
                maior2 = n
for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]:^6}]',end='')
    print()
print(f'A soma dos pares é: {somaPares}')
print(f'A soma dos valores da terceira coluna é: {somaColuna2}')
print(f'O maior valor da segunda linha é: {maior2}')