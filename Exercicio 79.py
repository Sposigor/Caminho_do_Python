Lista = [] # Lista para armazenar os dados
P = "" # Variavel pergunta

while True: # Força o laço
    N = int(input("Digite um valor: ")) # Variavel de saida
    if N in Lista: # Validação das repetições
        print("Valor duplicado, tente novamente")
    else: 
        Lista.append(N) # Método da lista para adicionar novos elementos
        print("Valor adicionado com sucesso!!")
    P = input("Você deseja continuar? [S/N] ").strip().upper() # Variavel
    while P not in "SN": # Laço para digitos diferentes de S ou N
        print("Por gentileza digitar S ou N.")
        P = input("Você deseja continuar? [S/N] ").strip().upper() # Repetição da saida
    if P == "N": # Validação de para
        break
    
print(f"Você digitou os valores: {Lista}") # Sainda dos dados digitados

