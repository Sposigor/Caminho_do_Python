Total = Tot = Menor = Cont = 0
Barato = ""

print(" = " * 20)
print("LOJA DA ESQUINA, TEM TUDO E MAIS UM POUCO!!!")
print(" = " * 20)
while True:
    P = str(input("Produto: "))
    V = float(input("Preço: "))
    Cont += 1
    Total += V
    if V > 1000:
        Tot += 1
    if Cont == 1 or V < Menor:
        Menor = V
        Barato = P
    R = " "
    while R not in "SN":
        R = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if R == "N":
        break
print(f"FIM DO PROGRAMA")
print(f"O total da compra foi R${Total:.2f}")
print(f"Temos {Tot} produtos custando mais de R$1000,00")
print(f"O produto mais barato foi {Barato} e custa R${Menor:.2f}")
    
