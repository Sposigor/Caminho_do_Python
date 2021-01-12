n = int(input('Digite um valor para tabuada: '))

print('-'*16)

for i in range(0, 11):
    print(f'{n:>3} x {i:>2} = {n*i}')

print('-'*16)