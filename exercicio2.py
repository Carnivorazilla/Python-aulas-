import os
os.system ('cls')
import math

turno = input('Escreva seu turno como N(para noturno) ou D (para diurno)')
 

hrsdetrabalho = float(input('Escreva sua carga horária'))

if turno == 'N' : 
    totaln = hrsdetrabalho*45
    print(f'Você atualmente ganha R${totaln}')
else:
    totald = hrsdetrabalho*37.50
    print(f'Você atualmente ganha R${totald}')