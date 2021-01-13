def formata_moeda(valor):
    resultado = str(valor).replace('.', ',0')
    return resultado


def aumentar(valor, aumento):
    return formata_moeda(valor + (valor * (aumento / 100)))


def diminuir(valor, reducao):
    return formata_moeda(valor - (valor * (reducao / 100)))


def dobro(valor):
    return formata_moeda(valor * 2)


def metade(valor):
    return formata_moeda(valor / 2)


preco = float(input("Informe o preço: R$ "))


print(f"A metade de R${formata_moeda(preco)} é R${formata_moeda(metade(preco))}")
print(f"O dobro de R${formata_moeda(preco)} é R${dobro(preco)}")
print(f"Aumentando 10%, temos R${aumentar(preco, 10)}")
print(f"Reduzindo 13%, temos R${diminuir(preco, 10)}")