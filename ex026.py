#026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip()
la = frase.lower()

print('Sua frase possui {} letras A!'.format(la.count('a')))
print('A primeira letra a do seu nome aparece no {} caractere e a ultima aparece no {} caractere'.format(frase.find('a')+1,
    frase.rfind('a')+1))