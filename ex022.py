
#022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
#  - Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ')


print('Seu nome todo em maiusculo fica: {}!'.format(nome.upper()))
print('Seu nome todo em minusculo fica: {}!'.format(nome.lower()))
print('Seu nome tem {} letras!'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras!'.format(nome.find(' ')))