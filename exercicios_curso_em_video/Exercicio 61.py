print("Gerado de PA")
print("=" * 20)
P = int(input("Primeiro termo: "))
R = int(input("Razão: "))

T = P
C = 1

while C <= 10:
    print(f"{T}", end = " ")
    T += R
    C += 1
print("Fim")