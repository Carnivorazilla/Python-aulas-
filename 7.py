import os
os.system('cls')


nomes = []
notas = []

while True :
    nome = input('Digite o nome do aluno')
    n1 = float(input(f'digite a primeira nota de {nome}'))
    n2 = float(input(f'digite a segunda nota de {nome}'))
    media = (n1+n2)/2
    notas.append(media)
    nomes.append(nome)

    resp = input('Deseja continuar?').lower()
    if resp == 'n':
        break
print(10*'-')
for i, e in enumerate(nomes):
    print(f'[{i}] - {e}')

i= int(input('Digite o número do aluno: '))

result = 'aprovado' if notas[i] > 6 else result = 'reprovado'

print(f'o aluno {nome[i]} foi {result}')
print(f'Média foi: {notas[i]:.2f}')


