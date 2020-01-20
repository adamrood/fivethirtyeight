import sympy
import numpy as np
from collections import Counter
import pandas as pd

lotto_numbers = np.arange(1,71,1)
prime = []
for x in range(1,71):
    if sympy.isprime(x):
        prime.append(x)
        
lotto_numbers = np.setdiff1d(lotto_numbers,np.array(prime))

results = []
for x in lotto_numbers:
    for i in range(2, x + 1):
        if(x % i == 0):
            isprime = 1
            for j in range(2, (i //2 + 1)):
                if(i % j == 0):
                    isprime = 0
                    break
            results.append(x)

lotto_numbers = list(set(results))
lista = []
for x in range (1000000):
        numbers = np.random.choice(lotto_numbers, size=5, replace=False)
        lista.append([numbers,np.prod(numbers)])

print(Counter(list(zip(*lista))[1]).most_common(5))

lista_df = pd.DataFrame(lista)

print(lista_df[lista_df[1] == 19958400][0])

lista_df[lista_df[1] == 19958400].to_csv('U:\\fivethirtyeight\\lotto.csv')



print(np.random.randint(1,25,4))