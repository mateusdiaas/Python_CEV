nome = input('Escreva seu nome: ').upper()
if nome == 'MATEUS':
    print('Que nome lindo você tem!')
else:
    print('Que nominho sem graça!')
print('Seja bem vindo, {}!'.format(nome.title()))

n1 = float(input('Agora me diga quanto você tirou na primeira prova do trimestre: '))
print('Ok.')
n2 = float(input('Agora me diga quanto vc tirou na segunda prova do trimestre: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}!'.format(m))
if m >= 6.0:
    print('Parabéns, você nao está de recuperação!')
else:
    print('Ta burrinho hein! kkk pegou recuperação!')
print('\nAté mais!')
