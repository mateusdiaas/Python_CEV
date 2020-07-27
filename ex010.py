# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
# Considere R$1,00 = U$3,27

n1 = float(input('Quanto dinheiro voce tem na carteira?: '))
n2 = n1/3.27

print('Com R${:.2f} voce pode comprar US${:.2f}'.format(n1, n2))

