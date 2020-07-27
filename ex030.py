#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um numero qualquer: '))
n1 = n % 2
if n1 == 0:
    print('O numero que vc digitou é par')
else:
    print('O numero que vc digitou é impar')
