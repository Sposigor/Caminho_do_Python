import random as R
N = tuple(R.sample(range(100), 20))
print(f"Os valores sorteados são: {N}")
print(f"O maior valor é {max(N)} e o menor valor é {min(N)}")
