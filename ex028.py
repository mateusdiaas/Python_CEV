#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from typing import List

from random import randint #randomiza numeros inteiros
from time import sleep #Faz o computador esperar por um tempo determinado para processar o proximo passo

n1 = randint(0, 5)
print('Pensei em um numero entre 0 e 5')
n2 = int(input('Em qual numero eu pensei?: '))

print('PROCESSANDO...')
sleep(2)

if n1==n2:
    print('Parabéns, voce acertou! Eu pensei no numero {}!'.format(n1))
else:
    print('Infelizmente vc errou... eu pensei no numero {}!'.format(n1))
