print('__Condição de existência de um triângulo__')
la = float(input('Qual o lado a: '))
lb = float(input('Qual o lado b: '))
lc = float(input('Qual o lado c: '))
if la + lb > lc and la + lc > lb and lb + lc > la:
    print(f'Os lados {la}, {lb}, {lc} PODEM formar um triângulo!!')
else:
    print(f'Os lados {la}, {lb}, {lc} NÂO PODEM formar um triângulo!!')