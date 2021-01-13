import collections

def analisar (texto):
    quantidade = collections.Counter(texto.lower())
    quantidade_m = sum(quantidade.values())

    pro = [(letras, frequencia / quantidade_m) for letras, frequencia in quantidade.items()]
    pro = collections.Counter(dict(pro))
    comum = pro.most_common(15)
    for c, pro in comum:
        print(f"{c} => {pro * 100:.2f}")
