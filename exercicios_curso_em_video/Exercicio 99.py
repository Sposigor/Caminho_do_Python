from time import sleep


def maior(*num):
	tamanho = len(num)
	maior = 0
	print('-=' * 30)
	print('Analisando os valores passados...')
	for valor in num:
		print(f'{valor} ', end='', flush=True)
		sleep(0.5)
		if valor > maior:
			maior = valor
	print(f'Foram informados {tamanho} valores ao todo.')
	print(f'O maior valor informado foi {maior}')


maior(10, 9, 2, 8, 12)
maior(1, 7, 6, 4)
maior(9, 8)
maior(2)
maior()