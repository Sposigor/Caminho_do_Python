def dobro(preco):
    dobro = preco*2
    return dobro
def metade(preco):
    metade = preco*0.5
    return metade
def aumentar(preco):
    aumento = preco*1.10
    return aumento
def diminuir(preco):
    desconto = preco*0.90
    return desconto


preco = float(input('Digite o preco: R$ '))
print(f'A metade de {preco:.2f} é {metade:.2f}')
print(f'O dobro de {preco:.2f} é {dobro:.2f}')
print(f'Preço aumentou 10%, agora custa {aumentar:.2f}')
print(f'Ofereço um desconto de 10%, o preço passa para {diminuir:.2f}')