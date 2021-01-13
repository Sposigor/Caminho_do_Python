m = f = maiores = 0
while True:
    print('=' * 20)
    print('CADASTRE UMA PESSOA')
    print('=' * 20)
    idade = int(input('Digite a sua Idade:'))
    while idade < 1 or idade > 120:
        print('Você digitou uma idade inválida, digite a sua idade novamente')
        idade = int(input('Digite a sua Idade :'))
    if idade >= 18:
        maiores += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        print('Você digitou uma opção INVÁLIDA, digite novamente')
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        m += 1
    elif sexo == 'F' and idade < 20:
        f += 1
    print('-'*20)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        print('Opção inválida, digite novamente')
        print('-' * 20)
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'{maiores} pessoas são maiores de 18 anos\n{f} são mulheres com menos de 20 anos\n{m} são homens')