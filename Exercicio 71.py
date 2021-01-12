print(" = " * 10)
print("          Banco SOS")
print(" = " * 10)
V = int(input("Que valor você quer sacar? "))
for X in [50, 20, 10, 5, 1]:
    Q = V // X
    V = V % X
    if Q > 0:
        print(f"{Q} notas de {X}")

    