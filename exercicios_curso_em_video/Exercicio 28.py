import random
pc = random.randint(0, 5)
vc = int(input('Digite um número de 0 a 5:'))
if pc==vc:
    print('Você ganhou!!!')
else:
    print('O PC ganhou!!!')