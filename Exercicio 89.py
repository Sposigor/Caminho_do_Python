total = []
aluno = []
nota = []
while True:
    aluno.append(str(input('Nome: ')))
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota 2: ')))
    aluno.append(nota[:])
    nota.clear()
    total.append(aluno[:])
    aluno.clear()
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while (resp!= 'S') and (resp!= 'N'):
        resp = str(input('Resposta inválida. Quer continuar? [S/N]: ')).strip().upper()
    if resp=='N':
        break
print('='*58)
print('N°'+' '*18+'NOME'+' '*25+'MÉDIA'+' '*15)
print('='*58)
for i in range(0,len(total)):
    print(f'{i+1:^8}', end=' '*10)
    print(f'{total[i][0]:^15}', end=' '*10)
    media = (total[i][1][0]+total[i][1][1])/2
    print(f'{media:^15}')
print('='*58)
while True:
    ver= int(input('Mostrar nota de qual aluno? [Para finalizar 999]'))
    if ver==999:
        print('FINALIZANDO...')
    else:
        print(f'Notas {total[ver-1][0]} de são {total[ver-1][1]}.')
