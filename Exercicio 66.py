S = C = 0

while True:
    N = int(input("Digite um valor: [999 para parar] "))
    if N == 999:
        break
    C += 1
    S += N

print(f"A soma dos {C} valores é {S}")