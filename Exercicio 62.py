print("Gerado de PA")
print("=" * 20)
P = int(input("Primeiro termo: "))
R = int(input("Razão: "))

T = P
C = 1
V = 10

if V != 0:
    while C <= V:
        print(f"{T}", end = " ")
        T += R
        C += 1
        if C == V + 1: 
            print("PAUSE")
            Ta = int(input("Mais quantos termos adicionar? "))
            V = C + Ta
            if Ta == 0:
                break
print(f"Finalizado com {V} termos")