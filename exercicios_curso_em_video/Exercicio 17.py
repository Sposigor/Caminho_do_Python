import math

co = float(input('Insira o valor do cateto oposto: '))
ca = float(input('Insira o valor do cateto adjacente: '))

print(f'A hipotenusa é: {math.sqrt(co**2 +ca**2):.2f}')
