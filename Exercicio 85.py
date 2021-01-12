Lista = [[], []] # Lista
P = " " # Variavel 
while True: # Força o laço
    C = int(input("Digite o valor: ")) # Acrescentar um item na lista
    if C % 2 == 0: # Validação par
        Lista[0].append(C)
    elif C % 2 == 1: # Validação impar
        Lista[1].append(C)
    P = input("Quer continuar? [S/N] ").strip().upper() [0] # Validação para continuar ou parar
    if P == "N": # Condição para parar
        break
    while P not in "S": # Validar saida do usúario 
        P = input("Quer continuar? [S/N] ").strip().upper() [0] 
print(f"A lista completa de pares é {sorted(Lista[0])}") # Saida ordenada par
print(f"A lista completa de impares é {sorted(Lista[1])}") # Saida ordenada impar