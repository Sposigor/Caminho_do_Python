linhas = 3
colunas = 3
matriz = [[int(input(f'({linha},{coluna}) ')) for coluna in range(1,colunas+1)] for linha in range(1,linhas+1)]
for i in matriz:
    print(i)