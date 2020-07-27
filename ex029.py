#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma
# mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v = float(input('Qual foi a velocidade registrada?: '))

if v > 80:
    print('Você ultrapassou o limite de volcidade e terá que pagar uma multa de R$:{:.2f}!'.format(float((v - 80) * 7)))
else:
    print('Você esta dentro o limite de velocidade, PARABÉNS!')
