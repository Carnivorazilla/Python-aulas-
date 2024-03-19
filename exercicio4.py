import os
os.system ('cls')
import math

prestaçao = float(input('Digite o valor da sua prestação:'))
multa = float(input('Digite o valor da multa de atrasado:'))
dia = float(input('Digite a quantidade de dias de atraso:'))

total = prestaçao+(prestaçao*(multa/100)*dia)

print(f'Com a adição da multa, o valor da sua prestação agora é:R${total:.0f},00')