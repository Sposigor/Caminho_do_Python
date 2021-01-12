dados = []
pessoas = {}
soma = média = mulheres = homens = acm = abm = nm = 0

while True:
    pessoas["nome"] = str(input("nome: "))
    pessoas["idade"] = int(input("idade: "))
    soma += pessoas["idade"]
    while True:
        pessoas["sexo"] = str(input("sexo: ")).upper()[0]
        if pessoas["sexo"] in "MF":
            break
        else:
            print("digite apenas \"F\" ou \"M\"")
    dados.append(pessoas.copy())
    pessoas.clear()
    while True:
        c = str(input("\ncontinuar? ")).lower()[0]
        if c in "sn":
            break
        else:
            print("\ndigite apenas \"s\" ou \"n\".")
    if c in "n":
        break
print("-=" *35)
if len(dados) == 1:
    print("você registrou:",len(dados),"pessoa")
else:
    print("você registrou:",len(dados),"pessoas")

for m in dados:
    if m["sexo"] in "F":
        mulheres += 1
    if m["sexo"] in "M":
        homens += 1
if homens == 0:
    print("você não registrou nenhum homem.",end="")
elif homens == 1:
    print("o único homem registrado foi:",end="")
else:
    print("os homens registrados foram:",end="")

for h in dados:
    if h["sexo"] in "M":
        print("",h["nome"],end="")

if mulheres == 0:
    print("\nvocê não registrou nenhuma mulher.")
elif mulheres == 1:
    print("\na única mulher registrada foi:",end="")
else:
    print("\nas mulheres registradas foram:",end="")

for p in dados:
    if p["sexo"] in "F":
        print("",p["nome"],end="")

if not len(dados) <= 1:
    média = soma/len(dados)
    print(f"\na média de idade é de {média:5.2f}")

if média:
    for iam in dados:
        if iam["idade"] > média:
            acm += 1
        if iam["idade"] == média:
            nm += 1
        if iam["idade"] < média:
            abm += 1
    if acm == 1:
        print("\na pessoa que está acima da média é:",end="")
    elif acm > 1:
        print("\nas pessoas que estão acima da média são,",end="")
    elif acm == 0:
        print("\nnão há pessoas acima da média.",end="")
    if acm > 0:
        for acm1 in dados:
            if acm1["idade"] > média:
                print("",acm1["nome"],"idade:",acm1["idade"],end="")
    if nm == 1:
        print("\na pessoa que está na média é:",end="")
    elif nm > 1:
        print("\nas pessoas que estão na média são:",end="")
    elif nm == 0:
        print("\nnão há pessoas na média.",end="")
    if nm > 0:
        for nm1 in dados:
            if nm1["idade"] == média:
                print("",nm1["nome"],"idade:",nm1["idade"],end="")
    if abm == 1:
        print("\na pessoa que está abaixo da média é:",end="")
    elif abm > 1:
        print("\nas pessoas que estão abaixo da média são:",end="")
    elif abm == 0:
        print("\nnão há pessoas abaixo da média:",end="")
    if abm > 0:
        for abm1 in dados:
            if abm1["idade"] < média:
                print("",abm1["nome"],"idade:",abm1["idade"],end="")
print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")