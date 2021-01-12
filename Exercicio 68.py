import random as r
from random import randrange

print("=-" * 13)
print("VAMOS JOGAR PAR OU IMPAR")
print("=-" * 13)

C = int(r.choice(range(1, 10, 1)))
E = " "
F = 0

while True:
    V = int(input("Digite um valor: "))
    while E not in "PI":
        E = input("Par ou Impar? [P/I] ").strip().upper()[0]
    S = V + C
    print(f"Você jogou {V} e o compuatador {C} a soma é {S}.")
    if E == "P":
        if S % 2 == 0:
            print("Você venceu!!")
            F += 1
        else:
            print("Você perdeu!!")
            break
    elif E == "I":
        if S % 2 == 1:
            print("Você venceu!!")
            F += 1
        else:
            print("Você perdeu!!")
            break
    print("Vamos jogar novamente!!")
print(f"GAME OVER....\n", f"Você venceu {F} vezes.")
