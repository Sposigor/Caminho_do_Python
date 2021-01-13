peso = float(input('Quanto você pesa? (kg) '))
altura = float(input('Quanto você mede? (m) '))
imc = (peso / altura ** 2)
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc < 25:
    print('Você está no seu peso ideal')
elif imc < 30:
    print('Você está com sobrepeso')
elif imc < 40:
    print('Você está obeso')
else:
    print('Você está com obesidade mórbida')