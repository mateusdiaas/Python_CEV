#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input('Digite a distancia da viagem em km: '))

if dist > 200:
    print('O preço da sua vigem é {}'.format(dist * 0.45))
else:
    print('O preço da sua viagem é {}'.format(dist * 0.5))
