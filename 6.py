import os
os.system('cls')

num = []
maior = 0
while True:

    n = int(input('Digite um numero inteiro(digite 0 para sair)'))

    if n == 0: break
    num.append(n)
   

for n in num: #fica vendo qual numero é maior
    if n > maior:
        maior=n

media = sum(num)/len(num)
print(f'a média é {media:.2f}')
print(f'o maior numero digitado é {maior:.2f}')

print(num)