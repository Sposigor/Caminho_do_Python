Listagem = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120, "Canetas", 22.30, "Livro", 34.90)

print('--'*20)
print(f'{"LISTAGEM DE PREÇOS":^40}')

print('--'*20)            
for i in Listagem:
    if type(i) is str:
        print(f'{i:.<32}', end='')
    else:
        print(f'R$ {i:>5.2f}')
print('--'*20)

