# Importando bibliotecas necessarias
import datetime
import json
import requests
import pandas as pd

# API com a informação necessaria, fonte (https://docs.awesomeapi.com.br/api-de-moedas)
api = requests.get("http://economia.awesomeapi.com.br/json/all/USD-BRL")

# Tranformar o GET da API

api2 = json.loads(api.content)
sr = pd.Series(api2['USD'])
dolar = sr.to_frame().T
dolar.drop(['codein', 'name', 'varBid', 'pctChange', 'high', 'low', 'timestamp', 'code'], axis=1, inplace=True)
Venda = float(dolar['ask'][0])
Compra = float(dolar['bid'][0])
Hoje = datetime.date.today()

# Conversor

while True:
    q = input('Vender[V] ou Comprar[C]: ').strip().upper()
    while not q or q not in 'VC':
        print('Digite V para vender ou C para Comprar')
        q = input('Vender[V] ou Comprar[C]: ').strip().upper()
    if q == 'V':
        v = float(input("Quantos dolares você gostaria de vender: "))
        print(f'O valor de venda na {Hoje:%d, %b %Y} é {Venda}')
        print(f'O valor de venda é R${Venda} e o valor total da sua venda é R${Venda*v}')
        break
    else:
        c = float(input("Quantos dolares você gostaria de comprar: "))
        print(f'O valor de compra no dia {Hoje:%d, %b %Y} é {Compra}')
        print(f'O valor de compra é R${Compra} e o valor total da sua compra é R${Compra/c}')
        break
