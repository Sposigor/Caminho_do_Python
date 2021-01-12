n1 = float(input("Quantos centimetros tem o primeiro angulo? "))
n2 = float(input("Quantos centimetros tem o segundo angulo? "))
n3 = float(input("Quantos centimetros tem o terceiro angulo? "))
if n1 == n2 and n1 == n3:
    print("O triangulo formado é equilatero")
elif n1 == n2 or n2 == n3 or n1 == n3:
    print("O triangulo formado é isosceles")
else:
    print("O triangulo formado é escaleno")