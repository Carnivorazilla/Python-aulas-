import os
os.system('cls')

salario = float(input('Escreva o valor do seu salario'))
agua = float(input('Escreva o valor da sua conta de água'))
luz = float(input('Escreva o valor da sua conta de luz'))
net = float(input('Escreva o valor da sua conta de internet'))

contas = agua + luz + net

if salario >= contas:
    resto = salario - contas
    print(f'Após o pagamento das contas voce fica com R${resto}')
    
else:
    print('Salário insuficiente')