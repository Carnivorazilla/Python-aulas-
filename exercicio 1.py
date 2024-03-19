import os
os.system ('cls')
import math

lilb = float(input('Digite o valor da base menor'))
bigb = float(input('Digite o valor da base maior'))
h = float(input('Digite o valor da altura do tronco da pirâmide'))

vol = h/3*(bigb**2 + lilb**2 + math.sqrt(bigb**2 * lilb**2))

print(f'O volume da pirâmide é:{vol:.2f}')