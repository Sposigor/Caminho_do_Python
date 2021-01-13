a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
if a > b:
    print('O número {a} é maior que {b} ')
elif b > a:
    print(f'O número {b} é maior que {a} ')
else:
    print(f'Os números\033[31m {a}\033[m e \033[31m{b} \033[m são iguais! ')