print('=' * 35)
print('Programa Meu Python, Minha vida')
print('=' * 35)
casa = float(input('Qua o valor da casa? R$: '))
salario = float(input('Qual o seu salario? R$: '))
pres = int(input('Em quantos anos quer pagar? '))
pres1 = float(casa / (pres * 12))
sal = salario * 30 / 100
if pres1 > sal:
    print('Com o salario de R${:.2f}, seu emprestimo nao pode ser aprovado, sentimos muito.'.format(salario))
else:
    print('Com o salario de R${:.2f}, seu emprestimo pode ser aprovado, parabéns!!.'.format(salario))