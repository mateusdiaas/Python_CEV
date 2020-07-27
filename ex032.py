# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date

y = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual'))
if y == 0:
    y = date.today().year


if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print('O ano {} é bissexto!'.format(y))
else:
    print('O ano {} nao é bissexto'.format(y))
