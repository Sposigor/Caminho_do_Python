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


def resumo(valor, aumento=False, reducao=False):
    print('-' * 32)
    print('|', 'RESUMO DO VALOR'.center(28), '|')
    print('-' * 32)
    print(f'| Preço analisado |  {formata_moeda(valor):<9} |')
    print(f'| Metade do preço |  {metade(valor):<9} |')
    print(f'| Dobro do preço  |  {dobro(valor):<9} |')
    print(f'| {aumento}% de aumento |  {aumentar(valor, aumento):<9} |')
    print(f'| {reducao}% de redução |  {diminuir(valor, reducao):<9} |')
    print('-' * 32)

resumo(50)