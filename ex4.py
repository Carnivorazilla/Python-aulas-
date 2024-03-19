import os
os.system('cls')

def area(base,altura):
    return base*altura/2

base = float(input('Escreva a base do triangulo'))
altura = float(input('Escreva a altura do triangulo'))

print(f'a area do triangulo é:{area(base,altura)} cm')
print(f'a area do triangulo é:{area(2,2)} cm')
print(f'a area do triangulo é:{area(30,80)} cm')
print(f'a area do triangulo é:{area(200,500)} cm')