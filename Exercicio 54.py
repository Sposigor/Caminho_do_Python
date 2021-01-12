from datetime import date 

Me = 0 # referência de menores de idade
Ma = 0 # referência de maiores de idade

for T in range(1, 8): # Laço de repetição
    T += 1 # Soma + 1 para cada laço
    P = int(input(f"A pessoa {T}° nasceu em: ")) # Informação da saida
    if (date.today().year - P) < 18: # Condição para validar a maioridade
        Me += 1 # Soma na referêmcia de menores de idade
    else:
        Ma += 1 # Soma na referência de maiores de idade

print(f"Essa é a {Me} de pessoas que são MENORES de idade.") 
print(f"Essa é a {Ma} de pessoas que são MAIORES de idade.")
