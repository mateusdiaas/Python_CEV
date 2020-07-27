# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

from time import sleep

salario = float(input('Prezado funcionario, qual é o seu salario atual?: '))

if salario > 1250:
    aumento = salario * 1.1
else:
    aumento = salario * 1.15

print('Calculando reajuste salarial...')
sleep(2)
print('Seu novo salario sera de R$:{:.2f}!'.format(aumento))
