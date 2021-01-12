num = int(input("Digite um número: "))
contador = 0

for i in range(1, num + 1):
    if num % i == 0:
        contador += 1

print(f"O número {num} foi divisível {contador} vezes!")

if contador == 2:
    print("O número é primo")
else:
    print("O número não é primo")