x = float(input('Qual é o salário do funcionário? R$'))
if x > 1250:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(x, x*1.1))
else:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(x, x*1.15))