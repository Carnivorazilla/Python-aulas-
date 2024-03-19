import ex6

import os
os.system('cls')

catO = float(input('Escreva o cateto oposto'))
catA = float(input('Escreva o cateto adjascente'))

print(f'seno = {ex6.seno(catO,catA)}')
print(f'tangente = {ex6.tangente(catO,catA)}')
print(f'cosseno = {ex6.cosseno(catO,catA)}')
