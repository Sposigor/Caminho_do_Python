print("Analisando o maior e menor peso")

A = [] # Lista para armazenar os dados

for L in range(1,6): # Laço de repetição
    P = float(input(f"Peso da {L}° Pessoa: ")) # Informação da saida
    A += [P] # Acrescenta a informação da saida na lista

print(f"O maior peso é {max(A):.2f}Kg\n" # Exibir informações com os parametros da lista de maior(max) ou menor(min)
      f"O menor peso é {min(A):.2f}Kg")
