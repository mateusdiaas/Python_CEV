# Faca um programa que leia a largura e a altura de uma parede em metros, calcule sua area e a quantidade de tinta
# necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m^2

l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede '))
a2 = a * l
lt = a2 / 2
print('Sua parede tem a dimensao de {}x{} e sua area é de {}mquadrados!'.format(l, a, a2))
print('Para pintar sua parde voce precisara de {} litros de tinta'.format(lt))
