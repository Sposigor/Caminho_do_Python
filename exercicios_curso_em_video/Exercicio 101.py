from datetime import date

def voto(ano):
    idade = (date.today().year - ano)
    if idade < 18:
        print(f'Ainda falta {18 - idade} anos para começar a votar')
    else:
        print(f'Com {idade} anos já votou!!')

voto(int(input('Em que ano você nasceu: ')))