import os
os.system('cls')

numero = int(input('Escreva um número inteiro e positivo'))
cont = 0
while cont in range(numero+1):
    print(f'{numero}/{cont}')
    cont= cont + 1
    if cont >= 11:
        print('Acabou os numeros :(')
    