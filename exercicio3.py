import os 
os.system('cls')
import math

valor = float(input('Digite o valor da sua compra para verificar seu desconto'))

if valor <= 200 and valor > 0 :
    total = valor * 0.20
    desconto = valor - total
    print(f'O valor da sua compra é R${valor},mas voce é elegiveu a um desconto então agora é R${desconto}')
else:
  print(f'O total da sua compra é {valor}, você não tem direito a desconto')