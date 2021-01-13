prc = float(input('Qual valor das compras? R$ '))
print("""Forma de pagamento:
[1] A vista no dinnheiro ou cheque - 10% de desconto
[2] A vista no cartao - 5% de desconto
[3] 2x cartao - preço normal
[4] 3x ou mais no cartao - 20% de juros
""")
esc = int(input('Qual sua escolha de pagamento? '))
if esc == 1:
    print('O pagamento ficara no valor de {}'.format(prc*0.90))
elif esc == 2:
    print('O pagamento ficara no valor {} '.format(prc*0.95))
elif esc == 3:
    print('O pagamento será feito em duas parcelas de {:.2f} totalizando {}'.format((prc/2), prc))
elif esc == 4:
    vez = int(input('Em quantas vezes você quer pagar? '))
    if vez >= 4:
        print('O pagamento será feito em {} parcelas no valor de {} totalizando {}'.format(vez, (prc*1.20)/vez, prc*1.20))
    elif vez < 4:
        print('Opcao invalida, tente novamente')
else:
    print('Opção invalida, tente novamente')

