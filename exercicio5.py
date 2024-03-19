import os
os.system ('cls')
import math

angulo = float(input('Escreva um ângulo'))

angsen = math.sin(angulo)
angcos = math.cos(angulo)
angtan = math.tan(angulo)

print(f'Seu angulo tem valor de \n{angsen:.2f} em Seno, \n{angcos:.2f} em Cosseno \ne {angtan:.2f} em Tangente ')