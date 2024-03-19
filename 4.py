import os
os.system('cls')

nomes = []

for i in range(5):
    nome = input('Qual é o nome da pessoa?')
    nomes.append(nome)
print(10*'-')
n = int(input('Quem você quer exibir?'))
print (nomes[n])