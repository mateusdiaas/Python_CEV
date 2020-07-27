# Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo.

from time import sleep

r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmeto: '))

print('CALCULANDO...\n')
sleep(2)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com os segmentos indicados É POSSÍVEL formar um triangulo!')
else:
    print('Com os segmentos indicados NÃO É POSSÍVEL formar um trinagulo!')