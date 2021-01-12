E = str(input("Digite a expressão: "))
P = []

for S in E:
    if S == "(":
        P.append("(")
    elif S == ")":
        if len(P) > 0:
            P.pop()
        else:
            P.append(")")
            break
if len(P) == 0:
    print("Sua expressão é válida!!")
else:
    print("Sua expressão é invalida!!")