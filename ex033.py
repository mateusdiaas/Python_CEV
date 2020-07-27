# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))

if n1 >= n2 and n1 >= n3:
    maior = n1
if n2 >= n1 and n2 >= n3:
    maior = n2
if n3 >= n1 and n3 >= n2:
    maior = n3

if n1 <= n2 and n1 <= n3:
    menor = n1
if n2 <= n1 and n2 <= n3:
    menor = n2
if n3 <= n1 and n3 <= n2:
    menor = n3



print('\nDos tres numeros digitados:\no maior é {}\no menor é {}!'.format(maior, menor))
