# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
an = float(input('Digite um anuglo qualquer:'))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))


print('O seno do angulo é {}, seu cosseno é {} e sua tangente é {}!'.format(sen, cos, tan))
