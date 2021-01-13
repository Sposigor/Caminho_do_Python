import datetime

Lista = {"Nome" : "",
         "Ano" : int,
         "Carteira" : int,
         "Contratação" : int,
         "Salário" : float} # Dicionario para armazenar os dados

Lista[0] = input("Nome: ") # Informação da saida
Lista[1] = int(input("Ano de nascimento: ")) # Informação da saida
Hoje = datetime.datetime.now() # Ano atual, independente do ano que estamos
Data = Hoje.year - Lista[1] # Ano atual - Ano de nascimento
Lista[2] = int(input("Carteira de Trabalho (0 não tem): ")) # Informação da saida
if Lista[2] != 0: # Validação para novas opções
    Lista[3] = int(input("Ano de Contratação: ")) # Informação da saida
    Lista[4] = input("Salário: ") # Informação da saida
    print("\n" * 2) # Informação da saida
    print("=" * 25) # Informação da saida
    print(f"Nome tem o valor de {Lista[0]}.") # Informação da saida
    print(f"Idade tem o valor de {Data}") # Informação da saida
    print(f"CTPS tem o valor {Lista[2]}") # Informação da saida
    print(f"Contratação tem o valor de {Lista[3]}") # Informação da saida
    print(f"Salário tem o valor de {Lista[4]}") # Informação da saida
    print(f"Aposentadoria tem o valor de {Data + (Lista[3] + 35) - Hoje.year}") # Informação da saida
    print("=" * 25) # Informação da saida
else: # Validação não satisfez a condição
    print(f"Nome tem o valor de {Lista[0]}.") # Informação da saida
    print(f"Idade tem o valor de {Data}") # Informação da saida
    print(f"CTPS tem o valor {Lista[2]}") # Informação da saida