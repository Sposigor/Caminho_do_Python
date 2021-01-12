N = int(input('Valor: '))
print('Escolha uma conversão:\n'
'[1] para BINARIO\n'
'[2] para OCTAL\n'
'[3] para HEXADECIMAL')
O = int(input('Sua opção: '))
if O == 1:
    print(f'BINARIO {bin(N)}')
elif O == 2:
    print(f'OCTAL {oct(N)}')
elif O == 3:
    print(f'HEXADECIMAL {hex(N)}')
else:
    print('Opção invalida')