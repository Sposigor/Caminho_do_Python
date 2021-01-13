def leiaInt(msg=''):
    print('\n', '-' * 30, sep='')
    while True:
        num = input(msg)
        if num.replace('-', '', 1).isdigit():  # .isnumeric()
            return int(num)
            break
        print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')