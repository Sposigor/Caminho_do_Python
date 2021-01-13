import random, time, operator
from random import randint
from time import sleep


J1 = J2 = J3 = J4 = 0
Lista = {"J1" : randint(1, 6), "J2" : randint(1, 6), "J3" : randint(1, 6), "J4" : randint(1, 6)}
x = list()

print("Valores sorteados!!")

for i, v in Lista.items():

    print(f"Jogador {i}, jogou os dados e tirou {v}")
    time.sleep(1)

x = sorted(Lista.items(), key=operator.itemgetter(1), reverse = True)

print("RANKING DOS JOGADORES")
print("=" * 22)

for h, v in enumerate(x):
    print(f"{h + 1}° Lugar: {v[0]} com {v[1]}")
    sleep(1)
