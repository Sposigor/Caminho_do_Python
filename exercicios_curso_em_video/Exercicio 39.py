from datetime import date
ano = int(input('Ano de nascimento: '))
g = input('Masculino ou Femino [M/F]').strip().upper()
print(f'Quem nasceu em {ano} tem {date.today().year - ano} em {date.today().year}')
if g == 'M':
    if date.today().year - ano < 18:
        print(f'Falta {(18 - (date.today().year - ano))} anos para o alistamento')
        print(f'Seu alistamento será em {(18 - (date.today().year - ano)) + date.today().year}')
    else:
        print(f'Falta {(40 - (date.today().year - ano))} anos para o exame de prostata')
        print(f'A dedada será em {(40 - (date.today().year - ano)) + date.today().year}')
else:
    if date.today().year - ano < 18:
        print(f'Falta {(18 - (date.today().year - ano))} anos para fazer outras coisas menos alistamento obrigatorio')
        print(f'Seu aniversário de 18 anos será em {(18 - (date.today().year - ano)) + date.today().year}')
    else:
        print(f'Falta {(40 - (date.today().year - ano))} anos para menopausa')
        print(f'Próximo desse ano {(40 - (date.today().year - ano)) + date.today().year}')