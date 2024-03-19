import os
os.system 
import math

anos = float(input('Quantos anos de idade você tem?'))
mes = float(input('Quantos meses de idade você tem?'))
dia = float(input('Quantos dias de idade você tem?'))

anosres = anos*365
mesres = dia*30
total = mesres + anosres + dia
print(f'Você ja viveu {total} de dias!Parabéns :D')