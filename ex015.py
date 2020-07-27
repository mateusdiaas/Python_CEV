#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de
# dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e
# R$0,15 por Km rodado.

d = int(input('Por qauntos dias o caro permaneceu alugado?: '))
km = float(input('Qual foi a quilometragem utilizada?: '))
p = 60 * d + 0.15 * km
print('O valor a ser pago pelo aluguel do veiculo sera de R${:.2f}'.format(p))
