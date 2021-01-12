print("-" * 25)
print("Sequência de Fibonacci")
print("-" * 25)

F = 0
I = 1

N = int(input("Quantos termos você quer mostrar? "))

C = 3

print("", "~" * 75)
print(f"{F} => {I}", end = " ")
while C <= N:
    U = F + I
    print(f"=> {U}", end = " ")
    F = I
    I = U
    C += 1

print("\n","~" * 75)