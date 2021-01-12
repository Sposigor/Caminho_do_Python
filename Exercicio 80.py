Lista = []
for X in range (0,5):
    N = int(input("Digite um valor: "))
    if X == 0 or N > Lista[-1]:
        Lista.append(N)
        print("Adicionado ao final da lista!")
    else:
        P = 0
        while P < len(Lista):
            if N < Lista[P]:
                Lista.insert(P, N)
                print(f"Adicionando na posição {P} da lista...")
                break
            P += 1
print(" -= " * 15)
print(f"Os valores digitados são {Lista}")