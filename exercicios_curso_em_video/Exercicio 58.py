import sys, time, random

def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

for i in progressbar(range(100), "Carregando Sistema: ", 50):
    time.sleep(0.03) 

print("Bem vindo HUMANO!!!!")
print("Esse é o jogo mortal de adivinhação!!!")
print("Um acerto pode lhe salvar a vida, um erro pode lhe custar a vida")

T = 0 # Tentantivas a serem realizadas
P = "" # Guarda a informação da saida
L = random.choice(range(1, 10, 1)) # Escolha do sistema


print("Agora vamos começar, você possui três tentativas para acerta o número entre 1 á 10")

for i in progressbar(range(100), "Iniciando o Jogo: ", 50):
    time.sleep(0.05) 


while P != L and T < 3: # Inicio das tentativas, são permitidas 3
        P = int(input("Escolha seu número de 1 á 10...: "))
        T += 1 # Acrescenta + 1 para cada tentativa realizada

        for i in progressbar(range(100), "Verificando a informação: ", 50):
            time.sleep(0.01)

        if P == L: # Validação da respota
            print("SEU TOLO!!!! VOCÊ ME VENCEU AAAAAAAAAHHH.....Iniciando autodestruição....")
            for i in progressbar(range(100), "Autodestruição iniciada: ", 50):
                time.sleep(0.03)
            break

        if P != L: # Verefica a resposta
            print(f"Errou você tentou {T} de 3 tentantivas!!")
        if P < L: # Dica para o player
            print("Quase, você chegou perto MAS seu número é menor que o meu HAHAHAHAHA!")
        if P > L: # Dica para o player
            print("Quase, Quase.... NO ENTANTO seu número é maior que o meu....")
else: # Fim de jogo
    print("DIGA ADEUS...GAMER OVER")






