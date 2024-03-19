import os

soma = lambda a,b : a+b
subtracao = lambda a,b : a-b
multiplicacao = lambda a,b : a*b
divisao = lambda a,b : a/b





menu = ['Soma,','subtração', 'Multiplicação',"Divisão",'Sair']

while True:
    os.system('cls')
    print('calculadora de lambda')
    for n , item in enumerate(menu):
        print(f'[{n+1}] - {item}') 
    op = int(input('Digite uma opção'))
    if op == 5: break
    elif str(op) not in "1234": print('opção invalida')
    else: 
        n1 = float(input('Digite um numero'))
        n2 = float(input('Digite um numero'))
        if op ==1 :print(f'{n1} + {n2} = {soma(n1,n2)}')
        elif op ==2 :print(f'{n1} + {n2} = {subtracao(n1,n2)}')
        elif op ==3 :print(f'{n1} + {n2} = {multiplicacao(n1,n2)}')
        elif op ==4 :print(f'{n1} + {n2} = {divisao(n1,n2)}')
    input('\nEnter continua...')