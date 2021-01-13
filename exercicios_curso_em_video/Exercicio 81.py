Lista = []
C = 0
P = " "
while True:
    Lista.append(int(input("Digite o valor: ")))
    C += 1
    P = input("Quer continuar? [S/N] ").strip().upper() [0]
    if P == "N":
        break
    while P not in "S":
        P = input("Quer continuar? [S/N] ").strip().upper() [0] 
print(f"Você digitou {C} elemento(s)")
D = sorted(Lista, reverse=True)
print(f"Os valores em ordem descrecente são {D}")
if 5 in Lista:
    print("O valor 5 foi encontrado na lista")
else:
    print("O valor 5 não foi encontrado na lista")

