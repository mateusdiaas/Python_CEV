import math
c1 = float(input('Digite o valor de um dos catetos: '))
c2 = float(input('Digite o valor do outro cateto: '))
hip = ((c1**2) + (c2**2))**(1/2)
hip2 = math.hypot(c1, c2)
print('O valor da hipotenusa do triangulo é: {:.2f}!'.format(hip))

print('A hipotenusa calculada pelo modulo math.hypot é igual a {:.2f}'.format(hip2))
