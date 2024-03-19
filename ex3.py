import os
os.system('cls')
 
def imc_t(peso,altura):
    imc=peso/altura**2
    return imc

peso = float(input('Escreva seu peso'))
altura = float(input('Escreva sua altura'))

resultado = imc_t(peso,altura)

print(f'Seu imc é {resultado:.2f}')