import os 
os.system('cls')

def exibir(num,msg):
    print(f'A mensagem é: {msg}')
    print(f'O numero é: {num}')

msg = input('Escreva uma mensagem')
num = int(input(f'Escreva um numero'))

exibir(num, msg)
exibir(3,msg)