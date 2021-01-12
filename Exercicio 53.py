nome = input('Seu nome: ')
print(f'Seu nome é {nome} e o inverso é {" ".join(i[::-1]for i in nome.split())}')