import random, time # Biblioteca random para gerar números aleatorios e time para a pausa da execução

print("MEGA SENA DA VIRADA!!") # Informação da saida

Q = int(input("Quantos jogos você quer sortear: ")) # Variavel para o laço

print(f"Sorteando {Q} jogos") # Informação da saida

Y = [] # lista para armazenar informação
for I in range(1, Q): # Laço de repetição
    time.sleep(0.5) # Tempo de pausa da execução 
    Y = random.sample(range(100), 6) # Informação gerada aleatoria
    print(f"Jogo {I}°: {Y}") # Informação de saida

print("BOS SORTE!!") # Informação de saida

