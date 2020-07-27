# Faca um algoritmo que leio o preco de um produto e mostre seu novo preco com 5% de desconto.

p = float(input('Qual é o preco do produto?:'))
d = p * 0.95

print('O produto que vsa senhoria deseja comprar custa R${:.2f}, com desconto de 5% ele saira por R${:.2f}'.format(p, d))
