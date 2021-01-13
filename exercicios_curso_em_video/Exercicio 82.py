Lista = [] # Lista
P = " " # Variavel 
while True: # Força o laço
    Lista.append(int(input("Digite o valor: "))) # Acrescentar um item na lista
    P = input("Quer continuar? [S/N] ").strip().upper() [0] # Validação para continuar ou parar
    if P == "N": # Condição para parar
        break
    while P not in "S": # Validar saida do usúario 
        P = input("Quer continuar? [S/N] ").strip().upper() [0] 
print(f"A lista completa é {sorted(Lista)}") # Saida ordenada
Pa = [] # Lista Par
Im = [] # Lista Impar
for x in Lista: # Laço para verificar os valores da lista
    if x % 2 == 0: # Validação par
        Pa.append(x)
    elif x % 2 == 1: # Validação impar
        Im.append(x)

print(f"A lista completa de pares é {sorted(Pa)}") # Saida ordenada par
print(f"A lista completa de impares é {sorted(Im)}") # Saida ordenada impar

