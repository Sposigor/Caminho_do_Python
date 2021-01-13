
def notas(*x, sit=False):
    D = dict()
    D['Total'] = len(x)
    D['Maior'] = max(x)
    D['Menor'] = min(x)
    D['Média'] = sum(x)/len(x)
    if sit:
        if D['Média'] >= 7:
            D['Situação'] = 'BOA'
        elif D['Média'] >= 5:
            D['Situação'] = 'RAZOAVEL'
        else:
            D['Situação'] = 'RUIM'
    return D

resp = notas(10, 5, 7.5, 11, sit=True)
print(resp)