Lista = {"Nome" : [],
        "Gol" : list(),
        "Total" : int}

Lista["Nome"] = input("Nome do jogador: ")
K = Lista["Nome"]
V = int(input(f"Quantas partidas {K} jogou: "))
for x in range(0, V):
    Lista["Gol"].append(int(input(f"Quantos gols na partida {x}? ")))
Lista["Total"] = sum(Lista["Gol"])

print("=" * 75)
print(Lista)
print("=" * 75)

print(f"O campo nome tem o valor {K}")
print(f"O campo nome tem o valor {Lista['Gol']}")
print(f"O campo nome tem o valor {Lista['Total']}")

print("=" * 75)

print(f"O jogador {K} jogou {V} partidas.")
for x, y in enumerate(Lista["Gol"]):
    print(f"No jogo {x}°, fez {y} gols.")
print(f"Foi um total de {Lista['Total']} gols.")    