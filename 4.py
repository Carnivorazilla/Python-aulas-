import os
os.system('cls')


numeros = []
num_positivos = 0
num_negativos = 0


while valor >0:
    valor = float(input("Digite um valor real (ou 0 para sair): "))
    if valor == 0:
        break
    numeros.append(valor)


for num in numeros:
    if num > 0:
        num_positivos += 1
    elif num < 0:
        num_negativos += 1


menor_valor = min(numeros)


print(f"Quantidade de valores positivos: {num_positivos}")
print(f"Quantidade de valores negativos: {num_negativos}")
print(f"Menor valor: {menor_valor}")
