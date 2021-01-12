Lista = []

for X in range(0, 5):
    Lista.append(input(f"Digite um valor para posição {X}°: "))
print(f"Você digitou os valores: {Lista}")
print(f'O maior valor digitado foi {max(Lista)} nas posições ', end='')
for p, n in enumerate(Lista):
    if n == max(Lista):
        print(f'{p}... ', end='')
print(f'\nO menor valor digitado foi {min(Lista)} nas posições ', end='')
for p, n in enumerate(Lista):
    if n == min(Lista):
        print(f'{p}... ', end='')