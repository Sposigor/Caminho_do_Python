P = int(input("Primeiro valor: ")) # Armazena a saida
S = int(input("Segundo valor: ")) # Armazena a saida
E = 0 

while E != 5:
    print("\n[1] somar\n"
    "[2] multiplicar\n"
    "[3] maior\n"
    "[4] novos números\n"
    "[5] sair do programa")
    E = int(input("Qual opção: \n")) # Armazena a saida
    if E == 1:
        print(f"A soma de {P} + {S} é {P + S}")
    elif E == 2:
        print(f"A multiplicação de {P} x {S} é {P * S}")
    elif E == 3:
        print(f"O maior número é {max(P, S)}")
    elif E == 4:
        P = int(input("Primeiro valor: ")) # Armazena a saida
        S = int(input("Segundo valor: ")) # Armazena a saida
    elif E != 5 :
        print("Opção invalida")
        continue
print("Volte sempre!!")
