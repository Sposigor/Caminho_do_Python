T = ("Palavra", "Dicionario", "Amanhã", "Hoje", "Tim", "Maia", "Azul", "Da", "Cor", "Do", "Mar")
for P in T:
    print(f"\nNa palavra {P} tem as vogais: ", end = " ")
    for L in P:
        if L in "iouea":
            print(L, end = " ")
