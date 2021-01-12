A = input("Informe seu sexo: [M/F] ").strip().upper() 
if A == "M" or A == "F":
    print("Informação registrada com sucesso!!")
else:
    while A not in "MF":
        A = input("Informe corretamente o seu sexo: [M\F] ").strip().upper()
    print("Informação registrada com sucesso!!")


