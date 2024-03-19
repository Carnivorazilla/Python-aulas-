import os
os.system('cls')

nomes = []

for i in range(5):
    nome = input('Qual é o nome')
    nomes.append(nome)
print(nomes)
print(len(nomes))

nome = input('Digite o nome do usuário : ')
nomes.remove(nome)
print(nomes)
print(len(nomes))